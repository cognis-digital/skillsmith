#!/usr/bin/env python3
"""skillsmith forge — generate a large catalog of *self-taught* command skills.

Each skill teaches an agent how to program one thing: a shell command, a Python
stdlib module, a builtin, a git subcommand, or a command-structuring pattern. The
catalog is "self-taught" — the forge introspects the **real tool on this machine**
(`pydoc` for Python, `<cmd> --help`/`man` for CLI) so the content is grounded in
the installed reality, not hallucinated. Every skill is an immense, standalone
teaching document with frontmatter that passes `skillsmith lint`.

Stdlib only. Deterministic and resumable (existing skills are skipped).

    python forge/forge.py            # generate everything
    python forge/forge.py --limit 50 # quick sample

Output: skills/<domain>/<name>/SKILL.md
"""
from __future__ import annotations

import argparse
import builtins
import importlib
import inspect
import io
import os
import pydoc
import re
import subprocess
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "skills")
CAP = 6000  # cap the verbatim reference excerpt per skill

from forge.catalog import CLI_COMMANDS, GIT_SUBCOMMANDS, PATTERNS  # noqa: E402
from forge.recipes import PY_RECIPES  # noqa: E402


# --------------------------------------------------------------------------- utils
def kebab(*parts: str) -> str:
    s = "-".join(parts)
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)[:64].strip("-")


def clean_desc(text: str, fallback: str) -> str:
    """A single-line description, 20-1024 chars, safe for frontmatter (no #, no quotes)."""
    text = " ".join((text or "").split())
    text = text.replace('"', "'").replace("#", "").strip()
    if len(text) < 20:
        text = fallback
    text = text.replace('"', "'").replace("#", "")
    if len(text) < 20:
        text = (text + " — a self-taught command skill for agents.").ljust(20)
    return text[:1000].strip()


def frontmatter(name: str, description: str, tags: list) -> str:
    taglist = ", ".join(sorted({kebab(t) for t in tags if t}))
    return (f"---\nname: {name}\ndescription: \"{description}\"\n"
            f"version: 1.0.0\ntags: [{taglist}]\n---\n")


def write_skill(domain: str, name: str, description: str, tags: list, body: str) -> bool:
    d = os.path.join(OUT, domain, name)
    path = os.path.join(d, "SKILL.md")
    if os.path.exists(path):
        return False
    os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(frontmatter(name, description, tags) + "\n" + body.rstrip() + "\n")
    return True


def run_help(cmd: str) -> str:
    """Capture a command's own help text (the self-teaching step)."""
    for args in ([cmd, "--help"], [cmd, "-h"], ["man", cmd]):
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=6,
                               encoding="utf-8", errors="replace")  # nosec - read-only help
            out = (r.stdout or "") + ("\n" + r.stderr if r.returncode and r.stderr else "")
            out = out.strip()
            if len(out) > 40:
                if args[0] == "man":  # strip backspace-bold from man output
                    out = re.sub(r".\x08", "", out)
                return out[:CAP]
        except (OSError, subprocess.SubprocessError):
            continue
    return ""


def first_sentence(text: str) -> str:
    text = " ".join((text or "").split())
    m = re.split(r"(?<=[.!?])\s", text, maxsplit=1)
    return m[0] if m else text


# --------------------------------------------------------------------------- python
SKIP_MODULES = {"this", "antigravity", "__hello__", "__phello__", "idlelib",
                "turtle", "turtledemo", "tkinter", "lib2to3"}


def python_module_body(mod_name: str):
    try:
        mod = importlib.import_module(mod_name)
    except Exception:
        return None
    doc = inspect.getdoc(mod) or ""
    publics = [n for n in dir(mod) if not n.startswith("_")]
    funcs, classes, consts = [], [], []
    for n in publics:
        try:
            obj = getattr(mod, n)
        except Exception:
            continue
        if inspect.isclass(obj):
            classes.append(n)
        elif callable(obj):
            sig = ""
            try:
                sig = str(inspect.signature(obj))
            except Exception:
                sig = "(...)"
            funcs.append(f"{n}{sig}")
        elif not inspect.ismodule(obj):
            consts.append(n)
    # verbatim pydoc reference (immense, grounded)
    buf = io.StringIO()
    try:
        buf.write(pydoc.render_doc(mod, renderer=pydoc.plaintext))
    except Exception:
        buf.write(doc)
    reference = re.sub(r"\x08.", "", buf.getvalue())[:CAP]

    summary = first_sentence(doc) or f"The Python standard-library module `{mod_name}`."
    desc = clean_desc(f"Program with Python's {mod_name} module: {summary}",
                      f"Program with the Python standard-library module {mod_name}.")
    parts = [f"# Python: `{mod_name}`\n",
             "## Overview\n",
             (doc or f"`{mod_name}` is part of the Python standard library.").strip() + "\n",
             "## When to use\n",
             f"Reach for `{mod_name}` when your task calls for "
             f"{summary[:120].rstrip('.') or 'this capability'}. It ships with Python — "
             "no dependency to install, available on every interpreter.\n",
             f"## Import\n\n```python\nimport {mod_name}\n```\n"]
    if funcs:
        parts.append("## Key functions\n\n" + "\n".join(
            f"- `{mod_name}.{f}`" for f in funcs[:30]) + "\n")
    if classes:
        parts.append("## Key classes\n\n" + ", ".join(
            f"`{c}`" for c in classes[:30]) + "\n")
    if consts:
        parts.append("## Constants / attributes\n\n" + ", ".join(
            f"`{c}`" for c in consts[:30]) + "\n")
    parts.append(_python_recipe(mod_name, funcs, classes))
    parts.append("## Full reference (introspected from this machine)\n\n```\n"
                 + reference + "\n```\n")
    parts.append(f"## Related\n\nOther standard-library modules pair well with "
                 f"`{mod_name}`; explore the `python` domain of this catalog.\n")
    tags = ["python", "stdlib", "programming", mod_name.split(".")[0]]
    return kebab("python", mod_name), desc, tags, "\n".join(parts)


def _python_recipe(mod: str, funcs: list, classes: list) -> str:
    ex = funcs[0].split("(")[0] if funcs else (classes[0] if classes else "")
    call = f"{mod}.{ex}(...)" if ex else f"{mod}. ..."
    return textwrap.dedent(f"""\
    ## Structuring it in a program

    Import once at the top of the module, then call into it where you need it. A
    robust pattern wraps the call, handles the errors the module can raise, and
    keeps the interface small:

    ```python
    import {mod}

    def do_work(...):
        \"\"\"Use {mod} to accomplish one well-defined task.\"\"\"
        result = {call}
        return result
    ```

    - Read the reference below for the exact signatures and exceptions.
    - Prefer the highest-level function that does the job; drop to lower-level
      primitives only when you need the control.
    - Keep `{mod}` calls behind a small function so the rest of your code does not
      depend on its details.
    """)


def python_builtin_body(name: str):
    obj = getattr(builtins, name)
    doc = inspect.getdoc(obj) or ""
    kind = "class" if inspect.isclass(obj) else "function"
    sig = ""
    try:
        sig = str(inspect.signature(obj))
    except Exception:
        sig = ""
    try:
        reference = re.sub(r"\x08.", "", pydoc.render_doc(obj, renderer=pydoc.plaintext))[:CAP]
    except Exception:
        reference = doc
    summary = first_sentence(doc) or f"The built-in {kind} `{name}`."
    desc = clean_desc(f"Program with Python's built-in {name}: {summary}",
                      f"Program with the Python built-in {kind} {name}.")
    body = textwrap.dedent(f"""\
    # Python builtin: `{name}`

    ## Overview

    `{name}` is a Python built-in {kind} — always available, no import required.

    {doc or ''}

    ## Signature

    ```python
    {name}{sig}
    ```

    ## When to use

    Built-ins are the first tool to reach for: `{name}` is implemented in C, fast,
    and universally available. Use it before writing your own equivalent.

    ## Structuring it in a program

    ```python
    result = {name}(...)   # see the reference below for exact arguments
    ```

    Built-ins compose cleanly — chain them with comprehensions, `map`/`filter`, and
    the other builtins rather than reaching for a library.

    ## Full reference (introspected from this machine)

    ```
    {reference}
    ```
    """)
    return kebab("builtin", name), desc, ["python", "builtin", "programming"], body


# --------------------------------------------------------------------------- cli
def cli_body(name: str, meta: dict):
    help_text = run_help(name)
    curated = meta.get("desc", "")
    examples = meta.get("examples", [])
    related = meta.get("related", [])
    tags = meta.get("tags", []) + ["bash", "cli", "command-line"]
    desc = clean_desc(f"Program the {name} command: {curated}",
                      f"Program the {name} command-line tool in shell scripts and pipelines.")
    ex_block = "\n".join(f"```bash\n{e}\n```" for e in examples) or \
        f"```bash\n{name} --help\n```"
    rel = ", ".join(f"`{r}`" for r in related) or "other tools in the `bash` domain"
    ref = f"## Full reference (`{name} --help` on this machine)\n\n```\n{help_text}\n```\n" \
        if help_text else ("## Reference\n\n`--help` was not capturable on this host; "
                           "consult `man " + name + "` on a POSIX system.\n")
    body = textwrap.dedent(f"""\
    # Command: `{name}`

    ## Overview

    {curated}

    ## When to use

    Use `{name}` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    {ex_block}

    ## Structuring it in a program

    `{name}` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if {name} ... ; then
        echo "ok"
    else
        echo "{name} failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    {ref}
    ## Related

    {rel}
    """)
    return kebab("bash", name), desc, tags, body


def recipe_body(slug: str, r: dict):
    ex = "\n\n".join(f"**{label}**\n\n```python\n{code}\n```" for label, code in r["examples"])
    pit = "\n".join(f"- {p}" for p in r["pitfalls"])
    rel = ", ".join(f"`{x}`" for x in r["related"]) or "other recipes in the `python-recipe` domain"
    desc = clean_desc(r["desc"], f"A Python idiom: {r['title']}.")
    body = textwrap.dedent(f"""\
    # Python recipe: {r['title']}

    ## Overview

    {r['intro']}

    ## When to use

    {r['desc']}

    ## Worked examples

    {ex}

    ## Structuring it in a program

    Prefer this idiom where it applies — it is the way experienced Python
    programmers express the intent, and it reads clearly to the next maintainer.
    Keep each use small and obvious; reach for a plain, explicit alternative when
    the idiom would obscure rather than clarify.

    ## Pitfalls

    {pit}

    ## Related

    {rel}
    """)
    return kebab("py", slug), desc, ["python", "idiom", "recipe", "programming"], body


def git_body(sub: str, desc: str):
    help_text = run_help("git") and _git_help(sub)
    d = clean_desc(f"Program git {sub}: {desc}",
                   f"Use the git {sub} subcommand in version-control workflows.")
    ref = f"## Full reference (`git {sub} --help`)\n\n```\n{help_text}\n```\n" if help_text else ""
    body = textwrap.dedent(f"""\
    # Git: `git {sub}`

    ## Overview

    {desc}

    ## When to use

    `git {sub}` is part of an everyday version-control workflow. Know exactly what
    it changes before you run it — some git operations rewrite history.

    ## Worked example

    ```bash
    git {sub} --help     # read the options first
    git {sub} ...        # then run it deliberately
    ```

    ## Structuring it in a workflow

    Script git operations idempotently and check status between steps:

    ```bash
    git {sub} ... || {{ echo "git {sub} failed" >&2; exit 1; }}
    git status --short
    ```

    {ref}
    ## Related

    Other `git` subcommands in this catalog's `git` domain.
    """)
    return kebab("git", sub), d, ["git", "version-control", "cli"], body


def _git_help(sub: str) -> str:
    try:
        r = subprocess.run(["git", sub, "-h"], capture_output=True, text=True,
                           timeout=6, encoding="utf-8", errors="replace")  # nosec
        return ((r.stdout or "") + (r.stderr or "")).strip()[:CAP]
    except (OSError, subprocess.SubprocessError):
        return ""


# --------------------------------------------------------------------------- main
def generate(limit: int | None = None) -> dict:
    made = {"python": 0, "builtin": 0, "bash": 0, "git": 0, "pattern": 0, "recipe": 0}
    budget = limit or 10 ** 9

    def stop():
        return sum(made.values()) >= budget

    # 1) Python stdlib modules — 100% self-taught via pydoc.
    for mod in sorted(sys.stdlib_module_names):
        if stop():
            break
        if mod.startswith("_") or mod in SKIP_MODULES:
            continue
        try:
            res = python_module_body(mod)
        except Exception:
            res = None
        if res and write_skill("python", *res):
            made["python"] += 1

    # 2) Python builtins.
    for name in sorted(n for n in dir(builtins) if not n.startswith("_")):
        if stop():
            break
        obj = getattr(builtins, name)
        if not (inspect.isclass(obj) or callable(obj)):
            continue
        try:
            res = python_builtin_body(name)
        except Exception:
            continue
        if write_skill("python-builtin", *res):
            made["builtin"] += 1

    # 3) CLI commands (self-taught via --help/man).
    for name, meta in CLI_COMMANDS.items():
        if stop():
            break
        if write_skill("bash", *cli_body(name, meta)):
            made["bash"] += 1

    # 4) Git subcommands.
    for sub, desc in GIT_SUBCOMMANDS.items():
        if stop():
            break
        if write_skill("git", *git_body(sub, desc)):
            made["git"] += 1

    # 5) Command-structuring patterns (curated, immense).
    for name, meta in PATTERNS.items():
        if stop():
            break
        nm = kebab("pattern", name)
        desc = clean_desc(meta["desc"], f"A shell command-structuring pattern: {name}.")
        if write_skill("pattern", nm, desc,
                       ["pattern", "bash", "shell", "command-structure"], meta["body"]):
            made["pattern"] += 1

    # 6) Python idiom recipes (curated, immense).
    for slug, r in PY_RECIPES.items():
        if stop():
            break
        if write_skill("python-recipe", *recipe_body(slug, r)):
            made["recipe"] += 1

    return made


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Forge a catalog of self-taught command skills.")
    ap.add_argument("--limit", type=int, default=None, help="cap total skills (for sampling)")
    a = ap.parse_args(argv)
    made = generate(a.limit)
    total = sum(made.values())
    print(f"forged {total} skills -> {OUT}")
    for k, v in made.items():
        print(f"  {k:8} {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

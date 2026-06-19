/**
 * Minimal YAML-frontmatter reader.
 *
 * Supports the subset of YAML that skill frontmatter realistically uses:
 *   - `key: value` scalars (strings, numbers, booleans, null)
 *   - quoted strings ('...' and "...")
 *   - block lists:
 *       tags:
 *         - a
 *         - b
 *   - inline flow lists: tags: [a, b, c]
 *   - comments (# ...) on their own line or trailing a value
 *
 * This is intentionally small and dependency-free. It is NOT a general YAML
 * parser; it covers the shapes a skill manifest is expected to use.
 */

export type FrontmatterValue =
  | string
  | number
  | boolean
  | null
  | string[]
  | number[];

export interface FrontmatterDocument {
  /** Parsed frontmatter key/value map (empty object if no frontmatter block). */
  data: Record<string, FrontmatterValue>;
  /** The document body after the closing `---` fence. */
  body: string;
  /** Whether a frontmatter block was present at all. */
  hasFrontmatter: boolean;
}

export class FrontmatterError extends Error {
  /** 1-based line number within the source where the problem occurred. */
  readonly line: number;
  constructor(message: string, line: number) {
    super(`${message} (line ${line})`);
    this.name = "FrontmatterError";
    this.line = line;
  }
}

const FENCE = "---";

/**
 * Parse a markdown document with optional leading YAML frontmatter.
 * Frontmatter must start on the first line with `---` and close with `---`.
 */
export function parseFrontmatter(source: string): FrontmatterDocument {
  // Normalize line endings so CRLF files parse identically.
  const normalized = source.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  const lines = normalized.split("\n");

  if (lines.length === 0 || lines[0].trim() !== FENCE) {
    return { data: {}, body: normalized, hasFrontmatter: false };
  }

  // Find the closing fence.
  let closeIndex = -1;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === FENCE) {
      closeIndex = i;
      break;
    }
  }
  if (closeIndex === -1) {
    throw new FrontmatterError("Unterminated frontmatter block (no closing '---')", 1);
  }

  const fmLines = lines.slice(1, closeIndex);
  const body = lines.slice(closeIndex + 1).join("\n");
  const data = parseBlock(fmLines, 1);

  return { data, body, hasFrontmatter: true };
}

/**
 * Parse the frontmatter lines into a key/value map.
 * `lineOffset` is the source line number of the first frontmatter content line
 * (used for error reporting).
 */
function parseBlock(
  fmLines: string[],
  lineOffset: number,
): Record<string, FrontmatterValue> {
  const data: Record<string, FrontmatterValue> = {};
  let i = 0;

  while (i < fmLines.length) {
    const raw = fmLines[i];
    const lineNo = lineOffset + i + 1;
    const trimmed = raw.trim();

    // Skip blank lines and full-line comments.
    if (trimmed === "" || trimmed.startsWith("#")) {
      i++;
      continue;
    }

    if (raw[0] === " " || raw[0] === "\t") {
      throw new FrontmatterError(
        `Unexpected indentation; expected a top-level 'key:' entry`,
        lineNo,
      );
    }

    const colon = raw.indexOf(":");
    if (colon === -1) {
      throw new FrontmatterError(`Expected 'key: value' but found "${trimmed}"`, lineNo);
    }

    const key = raw.slice(0, colon).trim();
    if (key === "") {
      throw new FrontmatterError("Empty key", lineNo);
    }
    if (Object.prototype.hasOwnProperty.call(data, key)) {
      throw new FrontmatterError(`Duplicate key "${key}"`, lineNo);
    }

    const rest = stripComment(raw.slice(colon + 1)).trim();

    if (rest === "") {
      // Could be a block list on following indented lines, or an empty value.
      const { items, consumed } = readBlockList(fmLines, i + 1);
      if (items !== null) {
        data[key] = items;
        i += 1 + consumed;
        continue;
      }
      // Empty scalar → null.
      data[key] = null;
      i++;
      continue;
    }

    data[key] = parseScalarOrFlowList(rest, lineNo);
    i++;
  }

  return data;
}

/**
 * Read an indented block list starting at index `start`. Returns the parsed
 * items (string[]) and how many lines were consumed, or items=null if the next
 * lines are not a block list.
 */
function readBlockList(
  fmLines: string[],
  start: number,
): { items: string[] | null; consumed: number } {
  const items: string[] = [];
  let i = start;
  let consumed = 0;

  while (i < fmLines.length) {
    const raw = fmLines[i];
    const trimmed = raw.trim();
    if (trimmed === "" || trimmed.startsWith("#")) {
      // Blank/comment line: stop the list (only contiguous items belong).
      break;
    }
    const m = /^(\s+)-\s+(.*)$/.exec(raw);
    if (!m) break;
    const value = stripComment(m[2]).trim();
    items.push(unquote(value));
    i++;
    consumed++;
  }

  return { items: consumed > 0 ? items : null, consumed };
}

/** Parse a single scalar value, or an inline flow list like `[a, b, c]`. */
function parseScalarOrFlowList(text: string, lineNo: number): FrontmatterValue {
  if (text.startsWith("[")) {
    if (!text.endsWith("]")) {
      throw new FrontmatterError("Unterminated inline list (missing ']')", lineNo);
    }
    const inner = text.slice(1, -1).trim();
    if (inner === "") return [];
    return splitFlowList(inner).map((part) => unquote(part.trim()));
  }
  return parseScalar(text);
}

/** Split an inline flow-list body on commas, respecting quotes. */
function splitFlowList(inner: string): string[] {
  const parts: string[] = [];
  let buf = "";
  let quote: string | null = null;
  for (const ch of inner) {
    if (quote) {
      buf += ch;
      if (ch === quote) quote = null;
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      buf += ch;
      continue;
    }
    if (ch === ",") {
      parts.push(buf);
      buf = "";
      continue;
    }
    buf += ch;
  }
  if (buf.trim() !== "" || parts.length > 0) parts.push(buf);
  return parts;
}

/** Coerce a bare scalar token into string/number/boolean/null. */
function parseScalar(text: string): FrontmatterValue {
  if (
    (text.startsWith('"') && text.endsWith('"')) ||
    (text.startsWith("'") && text.endsWith("'"))
  ) {
    return unquote(text);
  }
  if (text === "true") return true;
  if (text === "false") return false;
  if (text === "null" || text === "~") return null;
  if (/^-?\d+$/.test(text)) return Number(text);
  if (/^-?\d*\.\d+$/.test(text)) return Number(text);
  return text;
}

/** Remove surrounding single/double quotes if present. */
function unquote(text: string): string {
  if (
    (text.startsWith('"') && text.endsWith('"') && text.length >= 2) ||
    (text.startsWith("'") && text.endsWith("'") && text.length >= 2)
  ) {
    return text.slice(1, -1);
  }
  return text;
}

/**
 * Strip a trailing `# comment` from a value, but only when the `#` is not
 * inside a quoted string and is preceded by whitespace (or starts the text).
 */
function stripComment(text: string): string {
  let quote: string | null = null;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quote) {
      if (ch === quote) quote = null;
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      continue;
    }
    if (ch === "#" && (i === 0 || /\s/.test(text[i - 1]))) {
      return text.slice(0, i);
    }
  }
  return text;
}

---
name: bash-go
description: "Program the go command: Build, run, and test Go programs and modules."
version: 1.0.0
tags: [bash, build, cli, command-line, language]
---

    # Command: `go`

    ## Overview

    Build, run, and test Go programs and modules.

    ## When to use

    Use `go` when your task matches what it does best (see Overview). In a
    script, prefer it over hand-rolled logic — these tools are battle-tested,
    fast, and composable through pipes.

    ## Worked examples

    ```bash
go build ./...
```
```bash
go test ./...
```
```bash
go run main.go
```

    ## Structuring it in a program

    `go` is a building block in a shell pipeline. Compose it with `|`, guard on
    its **exit code**, and quote your variables:

    ```bash
    set -euo pipefail
    if go ... ; then
        echo "ok"
    else
        echo "go failed with exit $?" >&2
        exit 1
    fi
    ```

    - Chain with `|` to pass output to the next stage.
    - Check `$?` (or use `set -e`) — a non-zero exit means failure.
    - Quote `"$variables"` to survive spaces and globs.

    ## Full reference (`go --help` on this machine)

```
Go is a tool for managing Go source code.

Usage:

	go <command> [arguments]

The commands are:

	bug         start a bug report
	build       compile packages and dependencies
	clean       remove object files and cached files
	doc         show documentation for package or symbol
	env         print Go environment information
	fix         apply fixes suggested by static checkers
	fmt         gofmt (reformat) package sources
	generate    generate Go files by processing source
	get         add dependencies to current module and install them
	install     compile and install packages and dependencies
	list        list packages or modules
	mod         module maintenance
	work        workspace maintenance
	run         compile and run Go program
	telemetry   manage telemetry data and settings
	test        test packages
	tool        run specified go tool
	version     print Go version
	vet         report likely mistakes in packages

Use "go help <command>" for more information about a command.

Additional help topics:

	buildconstraint build constraints
	buildjson       build -json encoding
	buildmode       build modes
	c               calling between Go and C
	cache           build and test caching
	environment     environment variables
	filetype        file types
	goauth          GOAUTH environment variable
	go.mod          the go.mod file
	gopath          GOPATH environment variable
	goproxy         module proxy protocol
	importpath      import path syntax
	modules         modules, module versions, and more
	module-auth     module authentication using go.sum
	packages        package lists and patterns
	private         configuration for downloading non-public code
	testflag        testing flags
	testfunc        testing functions
	vcs             controlling version control with GOVCS

Use "go help <topic>" for more information about that topic.
```

    ## Related

    `gcc`, `cargo`

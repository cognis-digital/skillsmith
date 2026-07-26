"""Curated seed data for the forge: CLI commands, git subcommands, and shell
command-structuring patterns. The forge enriches CLI/git entries with each tool's
own `--help` on the host; the descriptions/examples here give every skill a solid,
valuable core even when live help is unavailable.
"""
from __future__ import annotations


def _c(desc, examples, related, tags):
    return {"desc": desc, "examples": examples, "related": related, "tags": tags}


# name -> curated metadata (the forge adds live `--help` as the full reference)
CLI_COMMANDS = {
    # --- text processing ---
    "grep": _c("Search text for lines matching a regular expression. The workhorse of log analysis and code search.",
               ["grep -rn 'TODO' src/", "grep -iE 'error|warn' app.log", "ps aux | grep -v grep | grep nginx"],
               ["egrep", "rg", "sed", "awk"], ["text", "search", "regex"]),
    "sed": _c("Stream editor: transform text line-by-line with substitution, deletion, and insertion.",
              ["sed 's/foo/bar/g' file", "sed -n '10,20p' file", "sed -i.bak 's/\\r$//' file"],
              ["awk", "grep", "tr"], ["text", "stream", "regex"]),
    "awk": _c("Pattern-action language for structured text: split into fields and compute per-line.",
              ["awk '{print $1}' file", "awk -F, '{sum+=$3} END{print sum}' data.csv", "df | awk 'NR>1{print $5, $6}'"],
              ["sed", "cut", "grep"], ["text", "fields", "reporting"]),
    "cut": _c("Extract columns from each line by byte, character, or delimiter.",
              ["cut -d: -f1 /etc/passwd", "cut -c1-8 file", "echo a,b,c | cut -d, -f2"],
              ["awk", "paste", "column"], ["text", "columns"]),
    "tr": _c("Translate or delete characters from stdin — case folding, squeezing, set removal.",
             ["tr 'a-z' 'A-Z' < file", "tr -d '\\r' < dosfile", "tr -s ' ' < spaced"],
             ["sed", "col"], ["text", "characters"]),
    "sort": _c("Sort lines of text, numerically or lexically, with keys and uniqueness.",
               ["sort -n nums", "sort -k2,2 -t, data.csv", "sort -u names"],
               ["uniq", "comm", "shuf"], ["text", "ordering"]),
    "uniq": _c("Collapse or count adjacent duplicate lines (pair with sort).",
               ["sort f | uniq -c | sort -rn", "uniq -d dupes", "uniq -u once"],
               ["sort", "comm"], ["text", "dedup"]),
    "wc": _c("Count lines, words, bytes, and characters.",
             ["wc -l file", "ls | wc -l", "wc -c bigfile"], ["nl", "cat"], ["text", "count"]),
    "head": _c("Print the first N lines (or bytes) of input.",
               ["head -n 20 file", "head -c 100 file", "curl -s url | head"],
               ["tail", "sed"], ["text", "preview"]),
    "tail": _c("Print the last N lines, or follow a file as it grows (-f).",
               ["tail -n 50 app.log", "tail -f /var/log/syslog", "tail -c 200 file"],
               ["head", "less"], ["text", "logs", "follow"]),
    "cat": _c("Concatenate files to stdout; the simplest way to stream file content.",
              ["cat a b > c", "cat -n file", "cat <<'EOF'\ntext\nEOF"],
              ["tac", "less", "head"], ["text", "io"]),
    "tac": _c("Concatenate and print files in reverse line order.",
              ["tac file", "tac log | grep -m1 START"], ["cat", "rev"], ["text"]),
    "nl": _c("Number the lines of a file.", ["nl file", "nl -ba script.sh"], ["cat", "wc"], ["text"]),
    "paste": _c("Merge lines of files side by side, delimited.",
                ["paste a b", "paste -d, col1 col2", "paste -s -d+ nums"], ["cut", "join"], ["text"]),
    "join": _c("Relational join of two sorted files on a common field.",
               ["join a.txt b.txt", "join -t, -1 1 -2 1 x y"], ["paste", "comm"], ["text", "relational"]),
    "comm": _c("Compare two sorted files line by line (common vs unique).",
               ["comm -12 a b", "comm -23 a b"], ["diff", "join"], ["text", "compare"]),
    "column": _c("Format input into aligned columns.",
                 ["mount | column -t", "column -s, -t data.csv"], ["awk", "printf"], ["text", "format"]),
    "fold": _c("Wrap input lines to a given width.", ["fold -w 72 file"], ["fmt"], ["text"]),
    "fmt": _c("Reformat/rewrap paragraphs to a target width.", ["fmt -w 80 notes"], ["fold"], ["text"]),
    "rev": _c("Reverse the characters of each line.", ["echo abc | rev"], ["tac"], ["text"]),
    "expand": _c("Convert tabs to spaces.", ["expand -t4 file"], ["unexpand"], ["text"]),
    "split": _c("Split a file into pieces by size or line count.",
                ["split -l 1000 big part_", "split -b 10M blob chunk_"], ["csplit", "cat"], ["files"]),
    "diff": _c("Show line-by-line differences between two files.",
               ["diff -u old new", "diff -r dir1 dir2"], ["patch", "comm", "git"], ["files", "compare"]),
    "patch": _c("Apply a diff/patch to files.", ["patch -p1 < fix.patch"], ["diff", "git"], ["files"]),
    "tee": _c("Read stdin and write to both stdout and files — tap a pipeline.",
              ["make 2>&1 | tee build.log", "echo hi | sudo tee /etc/motd"], ["cat"], ["io", "pipeline"]),
    "jq": _c("Command-line JSON processor: filter, map, and reshape JSON.",
             ["jq '.items[].name' data.json", "curl -s api | jq -r '.[].id'", "jq 'keys' obj.json"],
             ["grep", "python"], ["json", "data"]),
    "xargs": _c("Build and run commands from stdin — the bridge from lists to commands.",
                ["find . -name '*.log' | xargs rm", "cat urls | xargs -n1 -P4 curl -O", "echo a b | xargs -n1 echo"],
                ["find", "parallel"], ["pipeline", "batch"]),
    # --- files & dirs ---
    "ls": _c("List directory contents with rich formatting and sorting options.",
             ["ls -la", "ls -lhS", "ls -lt --color"], ["find", "tree", "stat"], ["files"]),
    "find": _c("Recursively search a directory tree by name, type, size, time, and run actions.",
               ["find . -name '*.py'", "find . -type f -mtime -1", "find . -name '*.tmp' -delete"],
               ["fd", "grep", "xargs"], ["files", "search"]),
    "cp": _c("Copy files and directories.", ["cp -r src dst", "cp -a a b", "cp file{,.bak}"], ["mv", "rsync"], ["files"]),
    "mv": _c("Move or rename files and directories.", ["mv old new", "mv *.txt dir/"], ["cp", "rename"], ["files"]),
    "rm": _c("Remove files and directories (irreversible — be deliberate).",
             ["rm file", "rm -rf build/", "rm -i *.o"], ["rmdir", "trash"], ["files", "danger"]),
    "mkdir": _c("Create directories, with parents (-p).", ["mkdir -p a/b/c"], ["rmdir"], ["files"]),
    "rmdir": _c("Remove empty directories.", ["rmdir emptydir"], ["rm", "mkdir"], ["files"]),
    "ln": _c("Create hard and symbolic links.", ["ln -s target link", "ln a b"], ["cp"], ["files"]),
    "touch": _c("Create empty files or update timestamps.", ["touch newfile", "touch -t 202601010000 f"], ["stat"], ["files"]),
    "stat": _c("Show detailed file metadata (size, perms, times, inode).", ["stat file", "stat -c '%s %n' *"], ["ls", "file"], ["files"]),
    "file": _c("Identify a file's type by content, not extension.", ["file mystery", "file -i doc"], ["stat"], ["files"]),
    "chmod": _c("Change file permission bits (symbolic or octal).", ["chmod +x script.sh", "chmod 644 file", "chmod -R u+w dir"], ["chown", "umask"], ["files", "perms"]),
    "chown": _c("Change file owner and group.", ["chown user:group file", "chown -R www /srv"], ["chmod"], ["files", "perms"]),
    "du": _c("Estimate disk usage of files and directories.", ["du -sh *", "du -h --max-depth=1", "du -a | sort -rn | head"], ["df", "ncdu"], ["disk"]),
    "df": _c("Report filesystem disk space usage.", ["df -h", "df -i"], ["du", "lsblk"], ["disk"]),
    "tar": _c("Archive files into (and extract from) tarballs, often compressed.",
              ["tar -czf out.tgz dir/", "tar -xzf out.tgz", "tar -tzf out.tgz"], ["gzip", "zip"], ["archive"]),
    "gzip": _c("Compress or decompress files with gzip.", ["gzip big", "gzip -d big.gz", "gzip -k keep"], ["tar", "zcat"], ["archive"]),
    "zip": _c("Create and update zip archives.", ["zip -r out.zip dir", "zip out.zip a b"], ["unzip", "tar"], ["archive"]),
    "unzip": _c("Extract zip archives.", ["unzip out.zip", "unzip -l out.zip"], ["zip"], ["archive"]),
    "basename": _c("Strip directory and suffix from a path.", ["basename /a/b/c.txt .txt"], ["dirname"], ["paths"]),
    "dirname": _c("Strip the last component from a path.", ["dirname /a/b/c"], ["basename"], ["paths"]),
    "realpath": _c("Resolve a path to its absolute, canonical form.", ["realpath ./link"], ["readlink"], ["paths"]),
    "readlink": _c("Print the target of a symbolic link.", ["readlink -f link"], ["realpath", "ln"], ["paths"]),
    # --- processes & system ---
    "ps": _c("Report a snapshot of current processes.", ["ps aux", "ps -ef", "ps -o pid,%cpu,cmd"], ["top", "pgrep"], ["process"]),
    "top": _c("Live view of processes and resource usage.", ["top", "top -o %MEM"], ["htop", "ps"], ["process", "monitor"]),
    "kill": _c("Send a signal to a process by PID.", ["kill 1234", "kill -9 1234", "kill -TERM $(pgrep app)"], ["pkill", "killall"], ["process", "signal"]),
    "pkill": _c("Signal processes by name pattern.", ["pkill -f server.py", "pkill -9 chrome"], ["kill", "pgrep"], ["process"]),
    "pgrep": _c("Find process IDs by name pattern.", ["pgrep -fl python", "pgrep nginx"], ["ps", "pkill"], ["process"]),
    "jobs": _c("List shell background jobs.", ["jobs -l"], ["bg", "fg", "kill"], ["process", "shell"]),
    "nohup": _c("Run a command immune to hangups, detached from the terminal.", ["nohup ./run.sh &"], ["disown", "setsid"], ["process"]),
    "time": _c("Measure how long a command takes.", ["time make", "time ./script.sh"], ["hyperfine"], ["process", "bench"]),
    "watch": _c("Run a command periodically and show the output.", ["watch -n1 df -h", "watch 'ps aux | head'"], ["top"], ["monitor"]),
    "env": _c("Show or set environment variables for a command.", ["env", "env FOO=1 ./app", "env -i sh"], ["export", "printenv"], ["env"]),
    "printenv": _c("Print environment variable values.", ["printenv PATH", "printenv"], ["env"], ["env"]),
    "which": _c("Locate a command in PATH.", ["which python", "which -a node"], ["type", "command"], ["shell"]),
    "type": _c("Show how a name would be interpreted (builtin, alias, file).", ["type -a ls", "type cd"], ["which", "command"], ["shell"]),
    "date": _c("Print or set the system date and time, with formatting.", ["date +%Y-%m-%d", "date -u", "date -d '1 day ago'"], ["cal"], ["time"]),
    "sleep": _c("Pause for a given duration.", ["sleep 5", "sleep 0.5"], ["timeout", "watch"], ["time"]),
    "timeout": _c("Run a command with a time limit, killing it if it overruns.", ["timeout 10 ./slow", "timeout -s KILL 5 cmd"], ["sleep", "kill"], ["process"]),
    "seq": _c("Print a sequence of numbers.", ["seq 1 10", "seq 0 2 20", "seq -w 1 100"], ["yes", "for"], ["numbers"]),
    "yes": _c("Repeat a string until killed — feed prompts or generate load.", ["yes | rm -i *", "yes hello | head"], ["seq"], ["shell"]),
    "uname": _c("Print system/kernel information.", ["uname -a", "uname -m"], ["hostnamectl"], ["system"]),
    "hostname": _c("Show or set the system hostname.", ["hostname", "hostname -I"], ["uname"], ["system"]),
    "id": _c("Print user and group identity.", ["id", "id -u", "id -Gn"], ["whoami", "groups"], ["system"]),
    "whoami": _c("Print the effective username.", ["whoami"], ["id"], ["system"]),
    "uptime": _c("Show how long the system has been running and load averages.", ["uptime"], ["top", "w"], ["system"]),
    "free": _c("Show memory usage.", ["free -h", "free -m"], ["top", "vmstat"], ["system", "memory"]),
    # --- network ---
    "curl": _c("Transfer data to/from a URL — the universal HTTP client for scripts.",
               ["curl -s https://api/x", "curl -O https://host/file", "curl -X POST -d @body url"],
               ["wget", "http", "jq"], ["network", "http"]),
    "wget": _c("Download files over HTTP/FTP, with recursion and resume.",
               ["wget https://host/file", "wget -c bigfile", "wget -r -np site"], ["curl"], ["network", "download"]),
    "ssh": _c("Open a secure shell to a remote host and run commands.",
              ["ssh user@host", "ssh -i key host 'uptime'", "ssh -L 8080:localhost:80 host"],
              ["scp", "sftp", "ssh-keygen"], ["network", "remote"]),
    "scp": _c("Copy files securely between hosts over SSH.", ["scp file host:/path", "scp -r dir host:~"], ["ssh", "rsync"], ["network"]),
    "ping": _c("Test reachability of a host via ICMP.", ["ping -c4 host"], ["traceroute", "curl"], ["network"]),
    "dig": _c("Query DNS records.", ["dig example.com", "dig +short A host", "dig MX domain"], ["nslookup", "host"], ["network", "dns"]),
    "nc": _c("netcat: read/write raw TCP/UDP — test ports, move bytes.", ["nc -zv host 22", "nc -l 9000"], ["socat", "curl"], ["network"]),
    "netstat": _c("Show network connections, routes, and listening ports.", ["netstat -tulpn", "netstat -rn"], ["ss", "lsof"], ["network"]),
    "ss": _c("Modern socket statistics (replaces netstat).", ["ss -tulpn", "ss -s"], ["netstat"], ["network"]),
    # --- shell control ---
    "echo": _c("Print arguments to stdout.", ["echo hello", "echo -n no-newline", "echo -e 'a\\tb'"], ["printf"], ["shell", "io"]),
    "printf": _c("Formatted output — more predictable than echo.", ["printf '%s=%d\\n' k 3", "printf '%.2f\\n' 3.14159"], ["echo"], ["shell", "io"]),
    "read": _c("Read a line of input into shell variables.", ["read -r line", "read -p 'name: ' n", "while read -r l; do :; done < f"], ["mapfile"], ["shell", "input"]),
    "test": _c("Evaluate a conditional expression (the [ ] command).", ["[ -f file ] && echo yes", "[ \"$a\" = \"$b\" ]"], ["case", "expr"], ["shell", "logic"]),
    "expr": _c("Evaluate integer arithmetic and string operations.", ["expr 1 + 2", "expr length abc"], ["test", "bc"], ["shell", "math"]),
    "bc": _c("Arbitrary-precision calculator language.", ["echo '3/4' | bc -l", "bc <<< '2^10'"], ["expr", "awk"], ["math"]),
    "tee": _c("Read stdin and write to both stdout and files.", ["cmd | tee out.log"], ["cat"], ["io"]),
    "true": _c("Do nothing, successfully (exit 0) — loops and defaults.", ["while true; do :; done"], ["false", "yes"], ["shell"]),
    "false": _c("Do nothing, unsuccessfully (exit 1).", ["false || echo failed"], ["true"], ["shell"]),
    "sudo": _c("Execute a command as another user (usually root).", ["sudo apt update", "sudo -u www cmd"], ["su", "doas"], ["system", "perms"]),
    "cron": _c("Time-based job scheduler — run commands on a schedule.", ["crontab -e", "crontab -l"], ["at", "systemd"], ["schedule"]),
    "crontab": _c("Manage per-user cron schedules.", ["crontab -l", "crontab -e"], ["cron", "at"], ["schedule"]),
    "make": _c("Build automation: run targets whose prerequisites changed.", ["make", "make -j4", "make test"], ["cmake", "ninja"], ["build"]),
    "git": _c("Distributed version control — track, branch, and share code history.", ["git status", "git commit -am msg", "git log --oneline"], ["hg"], ["vcs"]),
    "docker": _c("Build, run, and manage containers.", ["docker build -t img .", "docker run --rm img", "docker ps"], ["podman", "kubectl"], ["container"]),
    "python": _c("Run the Python interpreter and scripts.", ["python script.py", "python -m http.server", "python -c 'print(1)'"], ["pip"], ["language"]),
    "pip": _c("Install and manage Python packages.", ["pip install pkg", "pip freeze", "pip install -e ."], ["python", "pipx"], ["python", "packaging"]),
}

# Additional commands (enriched by live --help where installed).
CLI_COMMANDS.update({
    "less": _c("Page through text a screen at a time, with search and navigation.",
               ["less bigfile", "cmd | less -R", "less +F log"], ["more", "tail", "vim"], ["text", "pager"]),
    "more": _c("Simple pager: view text one screen at a time.", ["more file", "ls | more"], ["less"], ["text", "pager"]),
    "vim": _c("Modal text editor — edit files and streams with powerful keystrokes.",
              ["vim file", "vim +10 file", "vim -d a b"], ["nano", "vi", "emacs"], ["editor"]),
    "nano": _c("Simple, beginner-friendly terminal text editor.", ["nano file", "nano +5 file"], ["vim"], ["editor"]),
    "mount": _c("Attach a filesystem to the directory tree.", ["mount /dev/sdb1 /mnt", "mount -o ro dev dir", "mount"], ["umount", "lsblk", "df"], ["filesystem"]),
    "umount": _c("Detach a mounted filesystem.", ["umount /mnt", "umount -l /mnt"], ["mount"], ["filesystem"]),
    "strace": _c("Trace system calls and signals a process makes — debugging's X-ray.",
                 ["strace ./prog", "strace -e trace=open -f cmd", "strace -p 1234"], ["ltrace", "gdb"], ["debug"]),
    "nslookup": _c("Query DNS name servers interactively or in batch.", ["nslookup example.com", "nslookup -type=MX domain"], ["dig", "host"], ["network", "dns"]),
    "openssl": _c("Cryptography toolkit: keys, certs, hashing, encryption, TLS testing.",
                  ["openssl rand -hex 16", "openssl x509 -in cert.pem -text", "openssl s_client -connect host:443"],
                  ["gpg", "ssh-keygen"], ["crypto", "security"]),
    "gpg": _c("Encrypt, decrypt, sign, and verify data with GnuPG.",
              ["gpg -c file", "gpg --verify sig file", "gpg --encrypt -r you file"], ["openssl", "age"], ["crypto"]),
    "base64": _c("Encode or decode data in base64.", ["base64 file", "base64 -d enc", "echo hi | base64"], ["xxd", "openssl"], ["encoding"]),
    "md5sum": _c("Compute and verify MD5 checksums.", ["md5sum file", "md5sum -c sums.txt"], ["sha256sum", "cksum"], ["hash", "integrity"]),
    "sha256sum": _c("Compute and verify SHA-256 checksums — the default for integrity.",
                    ["sha256sum file", "sha256sum * > SHA256SUMS", "sha256sum -c SHA256SUMS"], ["md5sum", "openssl"], ["hash", "integrity"]),
    "sha1sum": _c("Compute and verify SHA-1 checksums.", ["sha1sum file"], ["sha256sum"], ["hash"]),
    "cksum": _c("Compute a CRC checksum and byte count.", ["cksum file"], ["md5sum"], ["hash"]),
    "xxd": _c("Make a hex dump of a file, or reverse one back to binary.", ["xxd file | head", "xxd -r dump > bin", "xxd -p file"], ["od", "hexdump"], ["binary"]),
    "od": _c("Dump files in octal, hex, or other formats.", ["od -c file", "od -An -tx1 file"], ["xxd", "hexdump"], ["binary"]),
    "install": _c("Copy files and set permissions/ownership in one step.", ["install -m755 script /usr/local/bin/", "install -d dir"], ["cp", "chmod"], ["files"]),
    "mktemp": _c("Create a unique temporary file or directory safely.", ["tmp=$(mktemp)", "dir=$(mktemp -d)"], ["trap"], ["files", "temp"]),
    "dd": _c("Low-level copy and convert of raw data — images, blocks, byte-exact copies.",
             ["dd if=/dev/zero of=file bs=1M count=10", "dd if=disk.img of=/dev/sdb status=progress"], ["cp", "cat"], ["disk", "danger"]),
    "sync": _c("Flush filesystem buffers to disk.", ["sync"], ["dd"], ["disk"]),
    "shred": _c("Overwrite a file repeatedly to make recovery hard, then optionally delete.", ["shred -u secret", "shred -n3 -z file"], ["rm"], ["security", "files"]),
    "umask": _c("Set the default permission mask for newly created files.", ["umask", "umask 022"], ["chmod"], ["perms", "shell"]),
    "getfacl": _c("Show a file's POSIX access-control lists.", ["getfacl file"], ["setfacl", "chmod"], ["perms"]),
    "setfacl": _c("Set POSIX access-control lists on files.", ["setfacl -m u:bob:rw file"], ["getfacl"], ["perms"]),
    "nice": _c("Run a command with an adjusted scheduling priority.", ["nice -n10 heavy", "nice -n-5 important"], ["renice", "ionice"], ["process"]),
    "at": _c("Schedule a command to run once at a given time.", ["at now + 5 minutes", "echo 'job' | at 02:00"], ["cron", "sleep"], ["schedule"]),
    "perl": _c("Powerful text-processing language; a one-liner Swiss army knife.",
               ["perl -pe 's/a/b/g' file", "perl -ne 'print if /re/' file", "perl -e 'print 1+2'"], ["awk", "sed"], ["language", "text"]),
    "node": _c("Run JavaScript outside the browser with Node.js.", ["node app.js", "node -e 'console.log(1)'", "node --version"], ["npm", "deno"], ["language"]),
    "npm": _c("Install and manage Node.js packages and scripts.", ["npm install", "npm run build", "npm ci"], ["node", "yarn", "pnpm"], ["packaging"]),
    "go": _c("Build, run, and test Go programs and modules.", ["go build ./...", "go test ./...", "go run main.go"], ["gcc", "cargo"], ["language", "build"]),
    "rg": _c("ripgrep: extremely fast recursive regex search that respects .gitignore.",
             ["rg TODO", "rg -t py 'def '", "rg -l pattern"], ["grep", "ag", "fd"], ["search", "text"]),
    "sqlite3": _c("Run SQL against a self-contained SQLite database file.",
                  ["sqlite3 db.sqlite '.tables'", "sqlite3 db 'SELECT * FROM t'", "sqlite3 db < schema.sql"], ["psql", "mysql"], ["database", "sql"]),
    "kubectl": _c("Control Kubernetes clusters — inspect and manage workloads.",
                  ["kubectl get pods", "kubectl logs pod", "kubectl apply -f k8s.yaml"], ["helm", "docker"], ["container", "ops"]),
    "ffmpeg": _c("Convert, trim, and transform audio and video.",
                 ["ffmpeg -i in.mov out.mp4", "ffmpeg -i a.wav -ar 16000 b.wav", "ffmpeg -i v.mp4 -vf scale=640:-1 s.mp4"], ["convert"], ["media"]),
    "convert": _c("ImageMagick: convert and manipulate images from the command line.",
                  ["convert in.png -resize 50% out.png", "convert *.png doc.pdf", "convert img.jpg -quality 80 out.jpg"], ["ffmpeg"], ["media", "images"]),
    "pdftotext": _c("Extract plain text from a PDF.", ["pdftotext doc.pdf -", "pdftotext -layout doc.pdf out.txt"], ["pandoc"], ["documents"]),
    "dos2unix": _c("Convert line endings from DOS/Windows CRLF to Unix LF.", ["dos2unix file", "find . -name '*.sh' -exec dos2unix {} +"], ["tr", "sed"], ["text"]),
    "iconv": _c("Convert text between character encodings.", ["iconv -f latin1 -t utf-8 file", "iconv -l"], ["dos2unix"], ["text", "encoding"]),
    "csplit": _c("Split a file into sections determined by context lines/patterns.", ["csplit file '/^CHAPTER/' '{*}'"], ["split"], ["files", "text"]),
    "factor": _c("Print the prime factors of numbers.", ["factor 360", "seq 100 | factor"], ["bc"], ["math"]),
    "shuf": _c("Randomly permute lines, or sample from them.", ["shuf list", "shuf -n5 list", "shuf -i1-100 -n3"], ["sort", "seq"], ["random"]),
    "tsort": _c("Topologically sort a partial order given as pairs.", ["tsort deps.txt"], ["sort"], ["graph", "order"]),
    "pr": _c("Paginate and columnate text for printing.", ["pr -3 file", "pr -t -w80 file"], ["fmt", "column"], ["text", "format"]),
    "vi": _c("The classic modal editor (usually vim in disguise).", ["vi file"], ["vim", "nano"], ["editor"]),
    "cd": _c("Change the shell's current directory (a builtin).", ["cd /path", "cd -", "cd ~"], ["pushd", "popd"], ["shell", "navigation"]),
    "pushd": _c("Change directory and push the old one onto a stack.", ["pushd /tmp", "popd"], ["popd", "cd", "dirs"], ["shell", "navigation"]),
    "popd": _c("Pop a directory off the stack and change to it.", ["popd"], ["pushd", "dirs"], ["shell", "navigation"]),
    "export": _c("Mark a shell variable for export to child processes.", ["export PATH=$PATH:/opt/bin", "export EDITOR=vim"], ["env", "set"], ["shell", "env"]),
    "alias": _c("Create a shorthand name for a command.", ["alias ll='ls -la'", "alias -p"], ["type", "function"], ["shell"]),
    "source": _c("Execute a script in the current shell (so its variables persist).", ["source .env", ". ./lib.sh"], ["export", "exec"], ["shell"]),
    "exec": _c("Replace the shell with a command, or reassign its file descriptors.", ["exec bash", "exec > log 2>&1"], ["source"], ["shell", "process"]),
    "trap": _c("Register handlers for signals and shell events (builtin).", ["trap 'rm -f $tmp' EXIT", "trap 'echo INT' INT"], ["kill", "signal"], ["shell", "signal"]),
    "wait": _c("Wait for background jobs to finish (builtin).", ["long & wait", "wait $pid"], ["jobs", "bg"], ["shell", "process"]),
    "set": _c("Set shell options and positional parameters.", ["set -euo pipefail", "set -- a b c", "set -x"], ["shopt", "export"], ["shell"]),
    "shopt": _c("Toggle bash-specific shell behaviors.", ["shopt -s globstar", "shopt -s nullglob", "shopt"], ["set"], ["shell"]),
    "history": _c("Show and manipulate the shell command history.", ["history", "history 20", "!42"], ["fc"], ["shell"]),
    "mapfile": _c("Read lines of input into a bash array (aka readarray).", ["mapfile -t lines < file", "mapfile -t arr < <(ls)"], ["read", "arrays"], ["shell"]),
    "getconf": _c("Query system configuration values.", ["getconf PAGE_SIZE", "getconf -a"], ["ulimit"], ["system"]),
    "ulimit": _c("Show or set shell resource limits.", ["ulimit -n", "ulimit -c unlimited"], ["getconf"], ["shell", "limits"]),
    "cal": _c("Display a calendar.", ["cal", "cal 2026", "cal -3"], ["date"], ["time"]),
    "tput": _c("Query the terminfo database — colors, cursor moves, terminal size.", ["tput cols", "tput setaf 2", "tput bold"], ["stty"], ["terminal"]),
    "stty": _c("Show or change terminal line settings.", ["stty -a", "stty size", "stty -echo"], ["tput"], ["terminal"]),
})


GIT_SUBCOMMANDS = {
    "init": "Create a new git repository in the current directory.",
    "clone": "Copy an existing repository, including its full history, to your machine.",
    "status": "Show the working tree status: staged, unstaged, and untracked changes.",
    "add": "Stage changes for the next commit.",
    "commit": "Record staged changes as a new commit with a message.",
    "log": "Show the commit history, with formatting and filtering options.",
    "diff": "Show changes between commits, the index, and the working tree.",
    "branch": "List, create, or delete branches.",
    "checkout": "Switch branches or restore working-tree files.",
    "switch": "Switch branches (a clearer alternative to checkout).",
    "restore": "Restore working-tree files from a source (undo local changes).",
    "merge": "Join two or more development histories together.",
    "rebase": "Reapply commits on top of another base tip (rewrites history).",
    "reset": "Move HEAD and optionally the index/working tree to a state.",
    "revert": "Create a new commit that undoes a previous commit safely.",
    "stash": "Shelve dirty working-tree changes and restore a clean state.",
    "tag": "Create, list, and delete tags (named points in history).",
    "fetch": "Download objects and refs from another repository.",
    "pull": "Fetch from and integrate with another repo or branch.",
    "push": "Update remote refs with local commits.",
    "remote": "Manage the set of tracked repositories.",
    "cherry-pick": "Apply the changes introduced by an existing commit.",
    "show": "Show one object (commit, tag, tree) in detail.",
    "blame": "Show what revision and author last modified each line of a file.",
    "bisect": "Binary-search history to find the commit that introduced a bug.",
    "clean": "Remove untracked files from the working tree.",
    "config": "Get and set repository or global options.",
    "rm": "Remove files from the working tree and the index.",
    "mv": "Move or rename a file and stage the change.",
    "grep": "Search tracked files for a pattern.",
    "reflog": "Show a log of where HEAD and refs have been (recover lost commits).",
    "worktree": "Manage multiple working trees attached to one repository.",
    "submodule": "Manage repositories nested inside a repository.",
    "describe": "Give an object a human-readable name based on the nearest tag.",
    "shortlog": "Summarize git log output, grouped by author.",
}


def _p(desc, body):
    return {"desc": desc, "body": body}


PATTERNS = {
    "pipes": _p(
        "Connect commands with the pipe operator so one program's stdout becomes the next one's stdin.",
        """# Pattern: Pipes (`|`)

## Overview

A pipe connects the standard output of one command to the standard input of the
next, forming a data-processing assembly line. Each stage does one job; the
pipeline composes them. This is the single most important idea in shell programming.

## When to use

Whenever you can express a task as "produce a stream, then transform it step by
step": search, filter, count, reshape, summarize.

## How it works

```bash
producer | filter | transformer | consumer
```

Every stage runs concurrently; data flows as it is produced. The exit status of the
whole pipeline is the status of the **last** command unless `set -o pipefail` is on.

## Worked examples

```bash
# top 10 most common client IPs in an access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head

# count Python files, excluding the virtualenv
find . -name '*.py' -not -path './.venv/*' | wc -l

# extract and de-duplicate all URLs from a document
grep -oE 'https?://[^ ]+' page.html | sort -u
```

## Structuring it in a program

- Keep each stage single-purpose; if a stage grows complex, move it to a function
  or a small script and pipe into that.
- Turn on `set -o pipefail` so a failure in any stage fails the pipeline.
- Prefer streaming tools (`grep`, `awk`, `sed`) over buffering the whole input in
  memory.

## Pitfalls

- Without `pipefail`, `false | true` exits `0` — the first failure is hidden.
- A pipeline runs each stage in a **subshell**; variables set inside a piped
  `while read` loop do not persist after the pipeline. Use process substitution or
  a here-string to avoid the subshell.
""",
    ),
    "redirection": _p(
        "Redirect a command's input and output to and from files and other descriptors.",
        """# Pattern: Redirection (`>`, `>>`, `<`, `2>`, `&>`)

## Overview

Redirection wires a command's file descriptors to files instead of the terminal.
Descriptor 0 is stdin, 1 is stdout, 2 is stderr.

## Operators

- `> file` — send stdout to file (truncate).
- `>> file` — append stdout to file.
- `< file` — read stdin from file.
- `2> file` — send stderr to file.
- `2>&1` — send stderr to wherever stdout currently goes.
- `&> file` — send both stdout and stderr to file (bash).
- `2>/dev/null` — discard stderr.

## Worked examples

```bash
make > build.log 2>&1          # capture everything
./job 2>errors.log             # keep stderr separate
sort < unsorted > sorted       # both ends redirected
grep foo file 2>/dev/null      # silence permission noise
```

## Structuring it in a program

- Order matters: `>file 2>&1` differs from `2>&1 >file`. Redirections are applied
  left to right; `2>&1` copies the *current* target of fd 1.
- Log to a file and the screen at once with `... 2>&1 | tee run.log`.
- Use `exec > logfile 2>&1` at the top of a script to redirect everything after it.

## Pitfalls

- `>` truncates the file immediately, even if the command later fails — write to a
  temp file and `mv` on success when that matters.
""",
    ),
    "exit-codes": _p(
        "Use command exit status to drive control flow and signal success or failure.",
        """# Pattern: Exit codes and `$?`

## Overview

Every command returns an integer exit status: `0` means success, non-zero means
failure. Shell control flow (`&&`, `||`, `if`, `set -e`) is built on it.

## Worked examples

```bash
mkdir -p out && cd out          # only cd if mkdir succeeded
grep -q pattern file || echo "not found"   # run on failure
command; echo "exited $?"       # inspect the last status
```

## Structuring it in a program

```bash
set -euo pipefail   # exit on error, unset var, or pipeline failure

deploy() {
    build   || return 1
    upload  || return 2
    verify  || return 3
}
deploy; echo "deploy returned $?"
```

- Return meaningful codes from functions and scripts so callers can branch.
- Reserve `0` for success; use small distinct non-zero codes for distinct failures.
- `set -e` stops on the first error; combine with `trap` for cleanup.

## Pitfalls

- `$?` reflects only the **most recent** command — capture it immediately.
- Inside `if cmd; then`, `set -e` does not trigger on `cmd`'s failure by design.
""",
    ),
    "command-substitution": _p(
        "Capture a command's output into a variable or another command with $(...).",
        """# Pattern: Command substitution (`$(...)`)

## Overview

`$(command)` runs a command and substitutes its stdout in place, with trailing
newlines stripped. It is how you feed one command's result into another.

## Worked examples

```bash
today=$(date +%Y-%m-%d)
files=$(find . -name '*.log')
echo "commit $(git rev-parse --short HEAD)"
cd "$(dirname "$0")"            # move to the script's directory
```

## Structuring it in a program

- Always quote the expansion: `"$(...)"` — unquoted, the result is word-split and
  glob-expanded.
- Prefer `$( )` over backticks: it nests cleanly and is readable.
- For large output, pipe instead of substituting to avoid holding it all in memory.

## Pitfalls

- Command substitution runs in a subshell; variable assignments inside it do not
  leak out.
- Trailing newlines are trimmed — fine for scalars, surprising for exact bytes.
""",
    ),
    "process-substitution": _p(
        "Feed a command's output as if it were a file with <(...) and >(...).",
        """# Pattern: Process substitution (`<(...)`, `>(...)`)

## Overview

Process substitution presents a command's output (or input) as a filename, so tools
that expect files can consume streams — and you avoid subshell variable loss.

## Worked examples

```bash
diff <(sort a) <(sort b)            # compare two pipelines as files
comm -12 <(sort x) <(sort y)
while read -r line; do count=$((count+1)); done < <(grep foo file)
tee >(gzip > out.gz) >(wc -l) < input
```

## Structuring it in a program

- Use `< <(producer)` to feed a `while read` loop without a pipe, so variables set
  in the loop survive.
- Combine multiple `>(...)` consumers with `tee` to fan one stream out.

## Pitfalls

- Bash/zsh only (not POSIX `sh`).
- The substituted filename (e.g. `/dev/fd/63`) is valid only while the command runs.
""",
    ),
    "here-doc": _p(
        "Feed a multi-line block of text to a command's stdin with a heredoc.",
        """# Pattern: Here-documents (`<<EOF`)

## Overview

A heredoc streams a literal block of text into a command's stdin until a delimiter
line. Perfect for embedding config, SQL, or scripts inline.

## Worked examples

```bash
cat > config.yml <<'EOF'
name: app
port: 8080
EOF

mysql db <<SQL
SELECT count(*) FROM users;
SQL

ssh host bash <<'EOF'
uptime
df -h
EOF
```

## Structuring it in a program

- Quote the delimiter (`<<'EOF'`) to keep the body **literal** — no `$var` or
  backtick expansion. Unquote it to allow expansion.
- `<<-EOF` strips leading tabs so you can indent the heredoc with the code.

## Pitfalls

- The closing delimiter must be on its own line with no trailing spaces (and, for
  `<<-`, may be indented only with tabs).
""",
    ),
    "globbing": _p(
        "Match sets of filenames with shell wildcard patterns.",
        """# Pattern: Globbing (`*`, `?`, `[...]`, `**`)

## Overview

The shell expands wildcard patterns into matching filenames before the command
runs. This is filename generation, distinct from regular expressions.

## Operators

- `*` — any run of characters (not `/`).
- `?` — any single character.
- `[abc]` / `[a-z]` — one character from a set/range.
- `**` — recursive match (requires `shopt -s globstar` in bash).
- `{a,b}` — brace expansion (not a glob, but often used together).

## Worked examples

```bash
ls *.py                 # every python file here
cp img_?.png backup/    # single-digit variants
shopt -s globstar; ls **/*.md   # recursive
rm -- *.tmp             # -- guards against filenames starting with -
```

## Pitfalls

- An unmatched glob is passed through **literally** by default; set
  `shopt -s nullglob` to expand to nothing instead.
- Globs are not regex: `*.txt` is anchored to whole names, `.` is literal.
- Always quote variables; never quote the glob you want expanded.
""",
    ),
    "parameter-expansion": _p(
        "Transform shell variables inline: defaults, slicing, substitution, and case.",
        """# Pattern: Parameter expansion (`${...}`)

## Overview

Parameter expansion manipulates variable values without spawning external commands
— defaults, substrings, pattern removal, replacement, length, and case changes.

## Cheat sheet

```bash
${var:-default}    # value, or 'default' if unset/empty
${var:=default}    # assign default if unset, then expand
${var:?message}    # error out with message if unset
${#var}            # length
${var#prefix}      ${var##prefix}   # strip shortest/longest prefix
${var%suffix}      ${var%%suffix}   # strip shortest/longest suffix
${var/old/new}     ${var//old/new}  # replace first / all
${var:offset:len}  # substring
${var^^}  ${var,,} # upper / lower (bash)
```

## Worked examples

```bash
name=${1:?usage: script NAME}
base=${file%.*}          # drop extension
ext=${file##*.}          # keep extension
path=${PATH//:/$'\\n'}    # colons -> newlines
```

## Why it matters

It is faster and safer than shelling out to `sed`/`basename`/`tr` for simple string
work, and it has no subprocess or quoting surprises.
""",
    ),
    "conditionals": _p(
        "Branch on conditions with if/elif/else and the test operators.",
        """# Pattern: Conditionals (`if`, `[[ ]]`, `case`)

## Overview

Conditionals branch on the exit status of a test. Bash's `[[ ]]` is safer and more
capable than the POSIX `[ ]` command.

## Test operators

```bash
[[ -f path ]]   # file exists and is regular
[[ -d path ]]   # directory exists
[[ -z $s ]]     # string empty      [[ -n $s ]]  non-empty
[[ $a == $b ]]  # string equal      [[ $a != $b ]]
[[ $a =~ ^re ]] # regex match
(( n > 3 ))     # arithmetic comparison
```

## Worked examples

```bash
if [[ -f config.yml ]]; then
    load config.yml
elif [[ -f config.json ]]; then
    load config.json
else
    echo "no config" >&2
    exit 1
fi

case $1 in
    start) run ;;
    stop)  halt ;;
    *)     echo "usage: $0 {start|stop}"; exit 2 ;;
esac
```

## Pitfalls

- Inside `[ ]`, always quote `"$var"` to avoid word-splitting bugs; `[[ ]]` does not
  split, so it is preferred in bash.
- `==` is string comparison; use `(( ))` or `-eq` for numbers.
""",
    ),
    "loops": _p(
        "Repeat work with for, while, and until loops over lists and streams.",
        """# Pattern: Loops (`for`, `while`, `until`)

## Overview

Loops repeat a body over a list of items or until a condition changes. Choose the
form that fits the source of iteration.

## Worked examples

```bash
for f in *.log; do gzip "$f"; done          # over a glob
for i in $(seq 1 5); do echo "$i"; done     # over a sequence

while read -r line; do                       # over lines of input
    process "$line"
done < input.txt

until ping -c1 host &>/dev/null; do          # until a condition holds
    sleep 1
done
```

## Structuring it in a program

- Prefer `while read -r line; do ...; done < file` (or `< <(cmd)`) over
  `for x in $(cmd)` when items may contain spaces.
- Use `continue` to skip and `break` to exit early.
- For parallelism over a list, pipe into `xargs -P` instead of a serial loop.

## Pitfalls

- `for x in $(cat file)` splits on whitespace and globs — almost never what you
  want for lines. Read line by line instead.
""",
    ),
    "functions": _p(
        "Package reusable shell logic into named functions with local scope.",
        """# Pattern: Functions

## Overview

Functions name a block of shell code so you can reuse it, test it, and give your
script structure. Arguments arrive as `$1`, `$2`, ...; the return value is an exit
code.

## Worked examples

```bash
log() { printf '[%s] %s\\n' "$(date +%T)" "$*" >&2; }

retry() {
    local n=$1; shift
    local i
    for ((i=1; i<=n; i++)); do
        "$@" && return 0
        sleep "$i"
    done
    return 1
}

retry 3 curl -fsS https://flaky/endpoint
```

## Structuring it in a program

- Declare loop and temp variables `local` so functions do not clobber globals.
- Return status with `return N`; "return" data by printing it and capturing with
  `$(func)`.
- Keep functions small and single-purpose; compose them.

## Pitfalls

- Without `local`, every assignment is global — a classic source of action-at-a-
  distance bugs.
""",
    ),
    "arrays": _p(
        "Store and iterate lists safely with bash indexed and associative arrays.",
        """# Pattern: Arrays

## Overview

Arrays hold multiple values in one variable and, crucially, preserve elements that
contain spaces — unlike space-separated strings.

## Worked examples

```bash
files=(*.txt)                 # glob into an array
files+=("one more.txt")       # append
echo "${#files[@]}"           # count
for f in "${files[@]}"; do    # iterate safely (quoted!)
    echo "$f"
done

declare -A color              # associative array (bash 4+)
color[apple]=red
color[lime]=green
echo "${color[apple]}"
for k in "${!color[@]}"; do echo "$k=${color[$k]}"; done
```

## Pitfalls

- Always expand with `"${arr[@]}"` (quoted, `@`) to keep elements intact. `${arr[*]}`
  joins into one string; unquoted `${arr[@]}` re-splits and globs.
- `${arr[0]}` alone refers to the first element, not the whole array.
""",
    ),
    "strict-mode": _p(
        "Make scripts fail fast and loud with set -euo pipefail and a trap.",
        """# Pattern: Strict mode (`set -euo pipefail`)

## Overview

By default the shell plows on after errors and treats unset variables as empty.
Strict mode turns silent failures into loud, early ones — the single biggest
robustness win for a script.

## The incantation

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\\n\\t'
trap 'echo "error on line $LINENO (exit $?)" >&2' ERR
```

- `set -e` — exit on any unhandled non-zero command.
- `set -u` — error on use of an unset variable.
- `set -o pipefail` — a pipeline fails if any stage fails, not just the last.
- `trap ... ERR` — report where it died; add cleanup here too.

## Worked example

```bash
set -euo pipefail
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT        # always clean up
process > "$tmp"
mv "$tmp" result.txt
```

## Pitfalls

- Under `set -e`, a command whose failure you *expect* must be guarded:
  `cmd || true`, or put it in an `if`.
- `set -u` breaks `$1` when no arg is passed; use `${1:-default}`.
""",
    ),
    "trap-cleanup": _p(
        "Run cleanup and handle signals reliably with trap.",
        """# Pattern: Traps and cleanup (`trap`)

## Overview

`trap` registers commands to run when the shell receives a signal or on specific
pseudo-signals like `EXIT` and `ERR`. It is how you guarantee cleanup no matter how
a script ends.

## Worked examples

```bash
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT           # runs on normal exit, error, or Ctrl-C

trap 'echo "interrupted" >&2; exit 130' INT TERM

trap 'echo "failed at line $LINENO" >&2' ERR
```

## Structuring it in a program

- Put an `EXIT` trap right after you create a temp resource, so cleanup is bound to
  the resource's lifetime.
- Combine with strict mode: `ERR` reports, `EXIT` cleans up.
- Keep trap handlers short and non-failing.

## Pitfalls

- Later `trap` calls for the same signal replace earlier ones — set the full
  handler you want.
""",
    ),
    "xargs-parallel": _p(
        "Turn a list into many commands and run them in parallel with xargs -P.",
        """# Pattern: Parallelism with `xargs -P`

## Overview

`xargs` reads items from stdin and runs a command with them as arguments; `-P N`
runs up to N invocations concurrently. It is the simplest way to parallelize a
batch of independent tasks.

## Worked examples

```bash
# resize every image, 8 at a time, one file per invocation
ls *.png | xargs -P8 -n1 -I{} convert {} -resize 50% small/{}

# fetch many URLs concurrently
xargs -P4 -n1 curl -sO < urls.txt

# NUL-safe against weird filenames
find . -name '*.log' -print0 | xargs -0 -P4 gzip
```

## Structuring it in a program

- `-n1` gives one item per command; `-I{}` places the item explicitly.
- `-P0` uses as many processes as possible; pick a bound near your core count.
- Use `-print0` / `-0` to survive spaces and newlines in filenames.

## Pitfalls

- Parallel output interleaves; write to per-item files or add locking if order
  matters.
- Each parallel job's failure does not stop the others — check results afterward.
""",
    ),
    "quoting": _p(
        "Control word-splitting and expansion with single quotes, double quotes, and escaping.",
        """# Pattern: Quoting

## Overview

Quoting decides what the shell expands and how it splits words. Getting it right is
the difference between a robust script and one that breaks on a space or a `*`.

## Rules

- `'single'` — fully literal; nothing expands.
- `"double"` — expands `$var`, `$(cmd)`, `` `cmd` ``, but keeps the result as one
  word and prevents globbing.
- `\\` — escape the next character.
- Unquoted — expands **and** word-splits **and** globs. Rarely what you want for
  variables.

## Worked examples

```bash
echo "$HOME/my file"      # one argument, expanded
echo '$HOME stays literal'
rm -- "$path"             # survives spaces; -- stops option parsing
find . -name '*.py'       # quote the glob so find (not the shell) expands it
```

## The one rule to remember

> Quote every variable expansion — `"$var"`, `"${arr[@]}"`, `"$(cmd)"` — unless you
> have a specific reason to want splitting or globbing.

## Pitfalls

- Unquoted `$var` with an empty value can vanish entirely, shifting arguments.
""",
    ),
    "getopts": _p(
        "Parse short command-line options in a script with getopts.",
        """# Pattern: Option parsing (`getopts`)

## Overview

`getopts` is the shell builtin for parsing short options (`-v`, `-o file`) in a
portable, predictable way — better than hand-rolled `$1` inspection.

## Worked example

```bash
verbose=0 out=""
while getopts ":vo:h" opt; do
    case $opt in
        v) verbose=1 ;;
        o) out=$OPTARG ;;
        h) echo "usage: $0 [-v] [-o FILE]"; exit 0 ;;
        \\?) echo "unknown option -$OPTARG" >&2; exit 2 ;;
        :)  echo "-$OPTARG needs an argument" >&2; exit 2 ;;
    esac
done
shift $((OPTIND - 1))          # remaining args are positional
```

## Structuring it in a program

- A trailing `:` in the optstring (`o:`) means that option takes an argument, found
  in `$OPTARG`.
- A leading `:` enables silent error handling so you can print your own messages.
- `shift $((OPTIND-1))` leaves `$@` holding the positional arguments.

## Pitfalls

- `getopts` handles only single-dash short options; for `--long` options use a
  manual `case` loop or a tool like `getopt`.
""",
    ),
    "signals-jobs": _p(
        "Manage background jobs and signals: &, jobs, fg, bg, wait, kill.",
        """# Pattern: Background jobs and signals

## Overview

The shell can run commands in the background and coordinate them. Signals let you
interrupt, terminate, or notify processes.

## Worked examples

```bash
long_task &                 # start in background
pid=$!                      # remember its PID
jobs -l                     # list jobs
wait "$pid"                 # block until it finishes
echo "task exited $?"

server & sleep 1; kill -TERM $!   # start, use, stop
```

## Common signals

- `TERM` (15) — polite termination (default for `kill`).
- `INT` (2) — Ctrl-C.
- `KILL` (9) — unblockable, last resort (no cleanup runs).
- `HUP` (1) — terminal closed; often used to reload daemons.

## Structuring it in a program

- Capture `$!` right after `&` to track each background job.
- `wait` for all children before exiting so nothing is orphaned.
- Prefer `TERM` and let the process clean up; reserve `KILL` for the unresponsive.
""",
    ),
    "find-exec": _p(
        "Act on many files precisely by combining find with -exec or -print0.",
        """# Pattern: `find -exec` and safe batch actions

## Overview

`find` locates files by rich criteria; `-exec` (or piping `-print0` to `xargs -0`)
runs a command on each match. Together they are the safe way to act on many files.

## Worked examples

```bash
find . -name '*.bak' -delete
find . -type f -mtime +30 -exec gzip {} \\;      # one process per file
find . -type f -name '*.js' -exec eslint {} +   # batched, faster
find . -name '*.tmp' -print0 | xargs -0 rm      # NUL-safe pipeline
```

## Structuring it in a program

- `-exec cmd {} \\;` runs once per file; `-exec cmd {} +` batches many files per
  invocation (much faster).
- Combine predicates: `-type f -name '*.log' -size +1M -mtime -7`.
- Use `-print0 | xargs -0` when you also want parallelism (`-P`).

## Pitfalls

- Plain `find ... | xargs` breaks on spaces/newlines in names — always use
  `-print0`/`-0`.
- Test destructive finds first by swapping the action for `-print`.
""",
    ),
    "arithmetic": _p(
        "Do integer math in the shell with (( )) and $(( )).",
        """# Pattern: Arithmetic (`(( ))`, `$(( ))`)

## Overview

Bash evaluates integer arithmetic natively — no `expr` subprocess needed. `(( ))`
is a command (for conditions and side effects); `$(( ))` expands to a value.

## Worked examples

```bash
(( count++ ))               # increment
total=$(( a + b * c ))      # expression to value
(( n % 2 == 0 )) && echo even
for (( i = 0; i < 10; i++ )); do echo "$i"; done
hex=$(( 0xff ))             # bases: 0x, 0, 2#1010
```

## Operators

`+ - * / %`, comparison `< <= > >= == !=`, logical `&& || !`, bitwise `& | ^ << >>`,
ternary `a ? b : c`, and assignment forms `+= -= *=`.

## Pitfalls

- Integer only — for decimals use `bc -l` or `awk`.
- Inside `(( ))` you do **not** prefix variables with `$` (write `n`, not `$n`),
  though `$n` also works.
- Division truncates toward zero.
""",
    ),
    "stdin-stdout-stderr": _p(
        "Understand the three standard streams and route them deliberately.",
        """# Pattern: The three standard streams

## Overview

Every process starts with three open file descriptors: stdin (0) for input, stdout
(1) for normal output, stderr (2) for diagnostics. Keeping data on stdout and
messages on stderr is what makes tools composable.

## Worked examples

```bash
echo "result"           # -> stdout (fd 1), part of the data
echo "warning" >&2      # -> stderr (fd 2), not part of the data
program < input         # feed stdin from a file
program > out 2> err    # separate the streams

data=$(program 2>/dev/null)   # capture data, discard diagnostics
```

## Structuring it in a program

- Print **results** to stdout so they flow through pipes; print **logs, prompts,
  and errors** to stderr so they do not pollute the data.
- A well-behaved filter reads stdin, writes stdout, and reports problems on stderr
  with a non-zero exit.

## Pitfalls

- Mixing logs into stdout corrupts downstream parsing — the most common reason a
  pipeline "randomly" breaks.
""",
    ),
}

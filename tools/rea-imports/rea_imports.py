import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

REA_PACKAGE = "rea-agents@6.7.0"
IMPORT_PATTERN = "DLL::"


def rea_environment(args):
    env = dict(os.environ)
    env["GHIDRA_INSTALL_DIR"] = args.ghidra
    env["JAVA_HOME"] = args.java
    env["REA_GHIDRA_STARTUP_TIMEOUT_MS"] = str(args.timeout_ms)
    return env


def search_imports(npx, dll, env):
    return subprocess.run(
        [npx, "-y", REA_PACKAGE, "search", str(dll), IMPORT_PATTERN,
         "--kind", "procedures", "--provider", "ghidra", "--json"],
        capture_output=True, text=True, encoding="utf-8", env=env,
    )


def is_complete(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))["operation"] == "search_procedures"
    except (OSError, ValueError, KeyError, TypeError):
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Run REA's Ghidra procedure search for imported names on every engine module DLL, one JSON per DLL, resumable."
    )
    parser.add_argument("--binaries", required=True, type=Path, help="Engine Binaries\\Win64 folder")
    parser.add_argument("--out", required=True, type=Path, help="Folder for <Module>.search.json files")
    parser.add_argument("--ghidra", default=r"C:\tools\ghidra_12.1.4_PUBLIC", help="GHIDRA_INSTALL_DIR")
    parser.add_argument("--java", default=r"C:\tools\jdk-21.0.12.1+1", help="JAVA_HOME")
    parser.add_argument("--timeout-ms", type=int, default=1800000, help="REA_GHIDRA_STARTUP_TIMEOUT_MS")
    parser.add_argument("--prefix", default="UnrealEditor-", help="Module DLL name prefix, UE4Editor- for UE 4")
    parser.add_argument("--only", nargs="*", default=[], help="Module names to run, e.g. Core CoreUObject")
    args = parser.parse_args()

    npx = shutil.which("npx")
    if not npx:
        sys.exit("npx not found on PATH")
    args.out.mkdir(parents=True, exist_ok=True)
    env = rea_environment(args)

    dlls = sorted(args.binaries.glob(args.prefix + "*.dll"))
    if args.only:
        wanted = {args.prefix + m + ".dll" for m in args.only}
        dlls = [d for d in dlls if d.name in wanted]

    failures = []
    for index, dll in enumerate(dlls, 1):
        module = dll.stem[len(args.prefix):]
        target = args.out / f"{module}.search.json"
        if is_complete(target):
            print(f"[{index}/{len(dlls)}] {module} done earlier", flush=True)
            continue
        started = time.monotonic()
        result = search_imports(npx, dll, env)
        seconds = round(time.monotonic() - started)
        if result.returncode == 0:
            target.write_text(result.stdout, encoding="utf-8")
        if result.returncode == 0 and is_complete(target):
            print(f"[{index}/{len(dlls)}] {module} ok {seconds}s", flush=True)
            continue
        error_file = args.out / f"{module}.error.txt"
        error_file.write_text(result.stdout + "\n" + result.stderr, encoding="utf-8")
        target.unlink(missing_ok=True)
        failures.append(module)
        print(f"[{index}/{len(dlls)}] {module} FAILED {seconds}s, see {error_file}", flush=True)

    print(f"finished: {len(dlls) - len(failures)} ok, {len(failures)} failed {failures}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

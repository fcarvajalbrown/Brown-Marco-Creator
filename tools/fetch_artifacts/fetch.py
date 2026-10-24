import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
MANIFEST = HERE / "artifacts.json"


def resolve(dest):
    path = pathlib.Path(dest).expanduser()
    return path if path.is_absolute() else REPO / path


def download(entry, folder):
    subprocess.run(
        ["gh", "release", "download", entry["tag"], "--pattern", entry["asset"], "--dir", folder, "--clobber"],
        cwd=REPO,
        check=True,
    )
    return pathlib.Path(folder) / entry["asset"]


def merge_zip(archive_path, target, force):
    added = 0
    with zipfile.ZipFile(archive_path) as archive:
        for member in archive.infolist():
            out = target / member.filename
            if member.is_dir() or (out.exists() and not force):
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as src, open(out, "wb") as dst:
                shutil.copyfileobj(src, dst)
            added += 1
    return added


def fetch(entry, force):
    target = resolve(entry["dest"])
    unzip = entry.get("unzip", False)
    if not unzip and target.exists() and not force:
        print(f"skip {entry['asset']}: {target} already exists (use --force to replace)")
        return
    with tempfile.TemporaryDirectory() as tmp:
        downloaded = download(entry, tmp)
        if unzip:
            added = merge_zip(downloaded, target, force)
            print(f"merged {entry['asset']} -> {target}: {added} new files")
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(downloaded), target)
    print(f"fetched {entry['asset']} -> {target}")


def main():
    parser = argparse.ArgumentParser(description="Download the git-ignored files this repo needs from its GitHub release.")
    parser.add_argument("--force", action="store_true", help="replace files that already exist")
    args = parser.parse_args()
    for entry in json.loads(MANIFEST.read_text(encoding="utf-8")):
        fetch(entry, args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())

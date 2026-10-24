import argparse
import json
import subprocess
import time

WMUX = r"C:\Users\Pipe\AppData\Local\Programs\wmux\resources\cli-bin\wmux.cmd"
BASE = "https://dev.epicgames.com/documentation/en-us/unreal-engine/"


def fetch(slug, version, wait):
    url = f"{BASE}{slug}?application_version={version}"
    subprocess.run([WMUX, "browser", "open", url], check=True, capture_output=True)
    time.sleep(wait)
    out = subprocess.run([WMUX, "browser", "get-text"], check=True, capture_output=True, text=True, encoding="utf-8")
    return url, json.loads(out.stdout)["text"]


def main():
    parser = argparse.ArgumentParser(description="Print the text of an Epic Unreal Engine docs page through the wmux browser panel, which passes the site's browser check.")
    parser.add_argument("slug", help="Page slug, e.g. gameplay-framework-in-unreal-engine")
    parser.add_argument("--version", default="4.27")
    parser.add_argument("--wait", type=float, default=8.0, help="Seconds to let the page render")
    args = parser.parse_args()
    url, text = fetch(args.slug, args.version, args.wait)
    print(url)
    print(text)


if __name__ == "__main__":
    main()

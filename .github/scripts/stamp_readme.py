#!/usr/bin/env python3
import argparse, datetime as dt, json, re, sys, pathlib

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", required=True, help="Path to lychee JSON report")
    ap.add_argument("--readme", required=True, help="Path to README.md")
    ap.add_argument("--marker", required=True, help="Marker key, e.g., last_verified_all")
    return ap.parse_args()

def load_lychee_counts(path: pathlib.Path):
    if not path.exists():
        return None  # signal missing

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

    links = []
    if isinstance(data, dict) and "links" in data:
        links = data["links"]
    elif isinstance(data, list):
        links = data
    else:
        links = data.get("results", []) if isinstance(data, dict) else []

    total = ok = redirected = broken = 0
    for item in links:
        status = item.get("status")
        if isinstance(status, int):
            code = status
            if 200 <= code < 300:
                ok += 1
            elif 300 <= code < 400:
                redirected += 1
            else:
                broken += 1
            total += 1
        else:
            s = str(status or "").lower()
            if s in ("ok", "valid"):
                ok += 1; total += 1
            elif s in ("redirected",):
                redirected += 1; total += 1
            elif s in ("excluded", "skipped"):
                pass
            else:
                broken += 1; total += 1
    return total, ok, redirected, broken

def build_badge_line(ok, redirected, broken, fallback=False):
    today = dt.date.today().isoformat()
    if fallback:
        return f"> ❌ Link verification attempted on **{today}** — report unavailable (likely rate-limit or CI hiccup)."
    if broken == 0:
        return f"> ✅ Links last verified: **{today}** — OK: {ok}, Redirects: {redirected}, Broken: {broken}"
    else:
        return f"> 🔴 Links last verified: **{today}** — OK: {ok}, Redirects: {redirected}, Broken: {broken}"

def replace_marker(readme_text: str, marker_key: str, replacement_line: str):
    start = f"<!-- {marker_key}:start -->"
    end = f"<!-- {marker_key}:end -->"
    pattern = re.compile(rf"({re.escape(start)})(.*?){re.escape(end)}", flags=re.DOTALL)
    if not pattern.search(readme_text):
        block = f"{start}\n{replacement_line}\n{end}\n"
        return block + "\n" + readme_text
    return pattern.sub(lambda m: f"{m.group(1)}\n{replacement_line}\n{end}", readme_text)

def main():
    args = parse_args()
    report_path = pathlib.Path(args.report)
    readme = pathlib.Path(args.readme)

    counts = load_lychee_counts(report_path)
    if counts is None:
        line = build_badge_line(0, 0, 0, fallback=True)
    else:
        total, ok, redirected, broken = counts
        line = build_badge_line(ok, redirected, broken)

    original = readme.read_text(encoding="utf-8")
    updated = replace_marker(original, args.marker, line)

    if updated != original:
        readme.write_text(updated, encoding="utf-8")
        print("README updated.")
    else:
        print("No changes to README.")

if __name__ == "__main__":
    sys.exit(main())
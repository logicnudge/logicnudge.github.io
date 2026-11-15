"""Dependency-free source checks for the Logic Nudge static Learning Hub.

Usage: python scripts/site_audit.py index.html
Does not replace browser, accessibility, contrast, or published-link checks.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import sys
from urllib.parse import unquote


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def analyze_html(html):
    doc = Document()
    doc.feed(html)
    tags = doc.tags
    issues = []

    def report(rule, detail):
        issues.append({"rule": rule, "detail": detail})

    htmltags = [a for tag, a in tags if tag == "html"]
    if not htmltags or not htmltags[0].get("lang"):
        report("document-language", "HTML document needs a lang attribute")
    if sum(1 for tag, _ in tags if tag == "h1") != 1:
        report("single-h1", "Expected exactly one top-level h1")
    if not any(tag == "title" for tag, _ in tags):
        report("document-title", "Missing HTML title")
    if not any(tag == "meta" and a.get("name", "").lower() == "description" and a.get("content") for tag, a in tags):
        report("meta-description", "Missing description metadata")
    if not any(tag == "link" and "canonical" in a.get("rel", "").split() and a.get("href") for tag, a in tags):
        report("canonical", "Missing canonical URL")
    ids = [a["id"] for _, a in tags if a.get("id")]
    for id_, count in Counter(ids).items():
        if count > 1:
            report("duplicate-id", f"Duplicate element id: {id_}")
    targets = set(ids)
    for tag, a in tags:
        if tag == "img" and "alt" not in a:
            report("image-alt", f"Image without alt attribute: {a.get('src', '(empty)')}")
        if tag == "a" and a.get("href", "").startswith("#"):
            anchor = unquote(a["href"][1:])
            if anchor and anchor not in targets:
                report("internal-fragment", f"Broken same-page link: #{anchor}")
    return issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/site_audit.py /path/to/index.html", file=sys.stderr)
        return 2
    file = Path(sys.argv[1])
    if not file.is_file():
        print(f"File not found: {file}", file=sys.stderr)
        return 2
    issues = analyze_html(file.read_text(encoding="utf-8"))
    print(json.dumps({"file": str(file), "issues": issues, "status": "PASS" if not issues else "FAIL"}, indent=2))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())

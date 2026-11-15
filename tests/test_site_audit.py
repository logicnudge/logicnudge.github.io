import unittest
from scripts.site_audit import analyze_html

BASE = """<!doctype html><html lang="en"><head><title>Logic Nudge</title>
<meta name="description" content="Verified learning lessons">
<link rel="canonical" href="https://logicnudge.github.io/"></head>
<body><main id="lessons"><h1>Learn coding</h1><img src="mark.png" alt="LN logo">
<a href="#lessons">Go to lessons</a></main></body></html>"""


class QualityTests(unittest.TestCase):
    def test_valid_page_has_no_errors(self):
        self.assertEqual(analyze_html(BASE), [])

    def test_heading_language_and_metadata(self):
        broken = BASE.replace('lang="en"', "").replace("<h1>Learn coding</h1>", "")
        rules = {x["rule"] for x in analyze_html(broken)}
        self.assertTrue({"document-language", "single-h1"} <= rules)

    def test_broken_fragment_and_duplicate_id(self):
        broken = BASE.replace('href="#lessons"', 'href="#absent"').replace(
            "</main>", '<p id="lessons">Again</p></main>'
        )
        self.assertEqual(
            {x["rule"] for x in analyze_html(broken)},
            {"duplicate-id", "internal-fragment"},
        )

    def test_missing_alt(self):
        broken = BASE.replace(' alt="LN logo"', "")
        self.assertIn("image-alt", {x["rule"] for x in analyze_html(broken)})


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Offline package validation. Does not test model behavior."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CASES = ROOT / "evals" / "cases.json"
ALLOWED_PRIMARY = {
    "sentence", "bullets", "numbered_steps", "arrow_chain", "table",
    "mindmap", "flowchart", "chat_chain", "strict_format", "prose",
    "text_tree", "sections",
}

class SkillPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL.read_text(encoding="utf-8")
        cls.cases = json.loads(CASES.read_text(encoding="utf-8"))

    def test_frontmatter(self):
        match = re.match(r"\A---\n(.*?)\n---\n", self.content, re.S)
        self.assertIsNotNone(match, "SKILL.md needs YAML frontmatter")
        frontmatter = match.group(1)
        name = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
        description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
        self.assertIsNotNone(name)
        self.assertIsNotNone(description)
        self.assertEqual(name.group(1).strip(), "lmkn-clarity")
        self.assertRegex(name.group(1), r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name.group(1)), 64)
        self.assertGreater(len(description.group(1).strip()), 40)
        self.assertLessEqual(len(description.group(1)), 1024)
        self.assertEqual(len(re.findall(r"^name:", frontmatter, re.M)), 1)
        self.assertEqual(len(re.findall(r"^description:", frontmatter, re.M)), 1)

    def test_under_500_lines(self):
        self.assertLessEqual(len(self.content.splitlines()), 500)

    def test_required_topics(self):
        for term in ("Arrow chains", "Mindmaps", "Flowcharts",
                     "Conversation summary", "Honor user instructions",
                     "Preserve substance"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.content.lower())

    def test_references_present(self):
        for filename in ("references/routing.md", "references/visuals.md",
                         "references/examples.md", "evals/RUBRIC.md"):
            with self.subTest(filename=filename):
                self.assertTrue((ROOT / filename).is_file())
                self.assertIn(filename, self.content)

    def test_evaluation_data(self):
        self.assertGreaterEqual(len(self.cases), 15)
        ids = set()
        for case in self.cases:
            with self.subTest(case=case.get("id")):
                self.assertEqual(set(case), {
                    "id", "prompt", "primary", "must_include", "must_avoid"
                })
                self.assertNotIn(case["id"], ids)
                ids.add(case["id"])
                self.assertTrue(case["prompt"].strip())
                self.assertIn(case["primary"], ALLOWED_PRIMARY)
                self.assertTrue(case["must_include"])
                self.assertTrue(case["must_avoid"])
                self.assertTrue(all(isinstance(x, str) and x.strip()
                                    for x in case["must_include"] + case["must_avoid"]))

    def test_no_dependency_files_required(self):
        # The skill must work as instructions alone; scripts are optional.
        self.assertNotIn("pip install", self.content.lower())

if __name__ == "__main__":
    unittest.main(verbosity=2)

import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import bookconfig  # noqa: E402


def _ns(**kw):
    base = {"book": None}
    base.update(kw)
    return Namespace(**base)


class ResolveBookTests(unittest.TestCase):
    def test_default_is_skybound(self):
        book = bookconfig.resolve_book(_ns())
        self.assertEqual(book.story_dir, bookconfig.DEFAULT_STORY_DIR)
        # Skybound config supplies these once Task 7 lands; resolver must not crash
        # if the file is missing, so only assert the path shape here.
        self.assertTrue(str(book.story_dir).endswith("Murder-Mystery-Novel-Fantasy-LitRPG-Story"))

    def test_book_flag_overrides_dir(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "book.config.yaml").write_text(
                'slug: dummy\ntitle: Dummy Book\nauthor: A. N. Other\n'
                'story_dir: ignored\ndefault_draft: Draft_2\n',
                encoding="utf-8",
            )
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.story_dir, d)
            self.assertEqual(book.slug, "dummy")
            self.assertEqual(book.title, "Dummy Book")
            self.assertEqual(book.author, "A. N. Other")
            self.assertEqual(book.default_draft, "Draft_2")

    def test_missing_config_falls_back_to_dir_name(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.slug, d.name)
            self.assertEqual(book.default_draft, "Draft_1")

    def test_path_helpers(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.manuscript("Draft_3"), d / "manuscript" / "Draft_3")
            self.assertEqual(book.feedback("Draft_3"), d / "review" / "feedback_Draft_3")
            self.assertEqual(book.publishing(), d / "publishing")

    def test_inline_comment_and_quotes_stripped(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "book.config.yaml").write_text(
                'slug: "q"   # trailing comment\ntitle: \'Quoted Title\'\n',
                encoding="utf-8",
            )
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.slug, "q")
            self.assertEqual(book.title, "Quoted Title")

    def test_value_with_colon_is_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "book.config.yaml").write_text(
                'title: The Skybound Wyrm: A Cozy LitRPG Mystery\n',
                encoding="utf-8",
            )
            book = bookconfig.resolve_book(_ns(book=str(d)))
            self.assertEqual(book.title, "The Skybound Wyrm: A Cozy LitRPG Mystery")

    def test_default_reads_skybound_config(self):
        book = bookconfig.resolve_book(_ns())
        self.assertEqual(book.slug, "skybound-wyrm")
        self.assertEqual(book.title, "The Skybound Wyrm")
        self.assertEqual(book.author, "Theo Weyren")
        self.assertEqual(book.default_draft, "Draft_6")


if __name__ == "__main__":
    unittest.main()

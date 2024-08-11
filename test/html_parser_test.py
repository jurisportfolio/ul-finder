import unittest
from ul_finder_src.html_parser import UlExtractor


class UlCounterTest(unittest.TestCase):
    def test_handle_starttag(self):
        extractor = UlExtractor()
        extractor.handle_starttag("ul", None)
        extractor.handle_starttag("li", None)
        self.assertEqual(extractor.ul_counter, 1)
        self.assertEqual(extractor.li_counter, 1)
        self.assertEqual(extractor.stack.last(), {"ul": 1, "has_li": 1})

    def test_handle_endtag(self):
        extractor = UlExtractor()
        extractor.handle_starttag("ul", None)
        extractor.handle_starttag("li", None)
        extractor.handle_endtag("ul")
        self.assertEqual(extractor.ul_counter, 1)
        self.assertEqual(extractor.li_counter, 0)
        self.assertEqual(extractor.storage[-1], {"ul": 1, "has_li": 1})

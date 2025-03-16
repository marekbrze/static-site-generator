import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"html": "this is html", "test": "this is test"})
        html = node.props_to_html()
        self.assertEqual(html, 'html="this is html" test="this is test"')


if __name__ == "__main__":
    unittest.main()

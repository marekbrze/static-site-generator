import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"html": "this is html", "test": "this is test"})
        html = node.props_to_html()
        self.assertEqual(html, 'html="this is html" test="this is test"')

    def test_repr_test1(self):
        node = HTMLNode(props={"html": "this is html", "test": "this is test"})
        html = node.__repr__()
        self.assertEqual(
            html, "HTML NODE:\nprops: {'html': 'this is html', 'test': 'this is test'}"
        )

    def test_repr_test2(self):
        node = HTMLNode(tag="p", value="this is a paragraph")
        html = node.__repr__()
        self.assertEqual(html, "HTML NODE:\ntag: p\nvalue: this is a paragraph")


if __name__ == "__main__":
    unittest.main()

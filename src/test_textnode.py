import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url_mismatch(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.url, node2.url)

    def test_text_mismatch(self):
        node = TextNode(
            "This is a bold text node", TextType.BOLD, url="https://example.com"
        )
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)


if __name__ == "__main__":
    unittest.main()

import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text_to_html_normal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_link(self):
        node = TextNode("This is a text node", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "http://example.com"})
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_image(self):
        node = TextNode(
            "This is a text node", TextType.IMAGE, url="http://example.com/image.jpg"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props,
            {"src": "http://example.com/image.jpg", "alt": "This is a text node"},
        )
        self.assertEqual(html_node.value, "")


if __name__ == "__main__":
    unittest.main()

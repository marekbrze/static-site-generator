import unittest

from src.htmlnode import ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_parent_to_html_not_tag(self):
        node_children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode(tag=None, children=node_children)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "You need to specify tag!")

    def test_parent_to_html_not_children(self):
        node = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "You need to specify children!")

    def test_parent_to_html_not_children_and_tag(self):
        node = ParentNode(tag=None, children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception), "You need to specify tag and children!"
        )


if __name__ == "__main__":
    unittest.main()

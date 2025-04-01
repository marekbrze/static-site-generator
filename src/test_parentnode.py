import unittest

from htmlnode import ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_parent_to_html_not_tag(self):
        node_children = [LeafNode("b", "Bold text"),
                         LeafNode(None, "Normal text"),
                         LeafNode("i", "italic text"),
                         LeafNode(None, "Normal text"),]
        node = ParentNode(tag=None, children=node_children)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "You need to specify tag!")



if __name__ == "__main__":
    unittest.main()

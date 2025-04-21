import unittest

from src.htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
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

    # Prosty test z jednym dzieckiem
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # Test zawierający wnuki
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # Test pustego ParentNode
    def test_empty_parent_node(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    # Jeden z childrenów nie ma tagu
    def test_children_without_a_tag(self):
        child_node = LeafNode("", "Lorem ipsum")
        parent_node = ParentNode(tag="p", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p>Lorem ipsum</p>",
        )


if __name__ == "__main__":
    unittest.main()

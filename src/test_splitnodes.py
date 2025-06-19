import unittest

from src.split_nodes import split_nodes_delimiter
from src.textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_leaf_to_html_p(self):
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ]
            ],
        )


if __name__ == "__main__":
    unittest.main()

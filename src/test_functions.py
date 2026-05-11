from functions import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        code = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, code)

    def test_bold(self):
        node = TextNode("This is text with **bold text**", TextType.TEXT)
        bold = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, bold)

        
    def test_none(self):

        node = TextNode("This is text with no special word", TextType.TEXT)
        nospecial = [
            TextNode("This is text with no special word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, nospecial)
        
    def test_invalid_syntax(self):
        node = TextNode("This is text with an _invalid syntax", TextType.TEXT)

        self.assertRaises(Exception, split_nodes_delimiter, [node], "_", TextType.ITALIC)
        

if __name__ == "__main__":
    unittest.main()
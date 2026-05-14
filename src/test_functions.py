from functions import split_nodes_delimiter, split_nodes_image, split_nodes_links, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import unittest

class TestSplittingTextNode(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        code = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, code)

    def test_split_bold(self):
        node = TextNode("This is text with **bold text**", TextType.TEXT)
        bold = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, bold)
        
    def test_split_none(self):

        node = TextNode("This is text with no special word", TextType.TEXT)
        nospecial = [
            TextNode("This is text with no special word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, nospecial)
        
    def test_invalid_syntax(self):
        node = TextNode("This is text with an _invalid syntax", TextType.TEXT)

        self.assertRaises(Exception, split_nodes_delimiter, [node], "_", TextType.ITALIC)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [this is a link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("this is a link", "https://i.imgur.com/zjjcJKZ.png")], matches)

        

if __name__ == "__main__":
    unittest.main()
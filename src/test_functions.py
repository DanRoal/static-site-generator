from functions import *
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


class TestTextToTextNodes(unittest.TestCase):
    def test_ordered(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(expected, text_to_textnodes(text))

class MarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):

    def test_header(self):
        self.assertEqual(block_to_block_type("# Header 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Header 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Header 6"), BlockType.HEADING)

    def test_invalid_header(self):
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#NotHeader"), BlockType.PARAGRAPH)

    def test_code_block(self):
        code = """```
print("Hello world")
```"""     
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">quote"), BlockType.QUOTE)

    def test_unordered(self):
        self.assertEqual(block_to_block_type("- Element"), BlockType.UNORDERED_LIST)

    def test_ordered(self):
        self.assertEqual(block_to_block_type("1. first"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("9. ninth"), BlockType.ORDERED_LIST)

        

if __name__ == "__main__":
    unittest.main()
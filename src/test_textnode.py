import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
        self.assertEqual(node, node3)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Other text", TextType.BOLD)
        node3 = TextNode("Other text", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        


if __name__ == "__main__":
    unittest.main()
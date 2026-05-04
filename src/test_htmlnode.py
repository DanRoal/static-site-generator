import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_prop = {"href": "https://www.google.com", "target": "_blank"}
        node1 = HTMLNode("a", "This is a link", None, test_prop)
        node2 = HTMLNode("a", "This is a link", None, test_prop)
        node3 = HTMLNode("p", "This is a paragraph")
        node4 = HTMLNode("p", "This is a paragraph",None,None)

        self.assertEqual(node1, node2)
        self.assertEqual(node3, node4)
    
        blank = HTMLNode()
        blank2 = HTMLNode(None,None,None,None)
        self.assertEqual(blank,blank2)


    def test_noteq(self):
        test_prop = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode("a", "This is a link", None, test_prop)
        node2 = HTMLNode("a", "This is the same link", None, test_prop)
        node3 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)

    def test_props_to_html(self):
        test_prop = {"href": "https://www.google.com", "target": "_blank",}
        test_prop2 = {"href": "https://www.google.com",}
        node = HTMLNode("a", "This is a link", None, test_prop)
        node2 = HTMLNode("a", "This is the same link", None, test_prop)
        node3 = HTMLNode("a", "This is another link", None, test_prop2)
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertNotEqual(node2.props_to_html(), node3.props_to_html())


        


if __name__ == "__main__":
    unittest.main()
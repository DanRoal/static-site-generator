import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        test_props = {"href":"google.com"}
        leaf1 = LeafNode("a", "Hello, world!", test_props)
        leaf2 = LeafNode("a", "Hello, world!", test_props)
        self.assertEqual(leaf1, leaf2)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )  

    def test_to_html_with_several_children(self):
        grandgrandchild_node = LeafNode("i", "grandgrandchild")

        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = ParentNode("div", [grandgrandchild_node])
        grandchild_node3 = LeafNode("b", "grandchild3")

        child_node1 = ParentNode("span", [grandchild_node1])
        child_node2 = ParentNode("span", [grandchild_node2])
        child_node3 = ParentNode("span", [grandchild_node3])

        parent_node = ParentNode("div", [child_node1, child_node2])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b></span><span><div><i>grandgrandchild</i></div></span></div>",
        )  

        


if __name__ == "__main__":
    unittest.main()
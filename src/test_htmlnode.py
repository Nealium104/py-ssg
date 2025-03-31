import unittest
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div node")
        self.assertEqual(repr(node), "HTMLNode(Tag:div, Value:This is a div node, Children:None, Props:None)")
        node2 = HTMLNode("div", "This is a div node", None, {"href": "https://www.google.com"})
        self.assertEqual(repr(node2), "HTMLNode(Tag:div, Value:This is a div node, Children:None, Props:{'href': 'https://www.google.com'})")

    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div node")
        self.assertEqual(node.props_to_html(), "")
        node2 = HTMLNode("div", "This is a div node", None, {"class": "hi-there", "href": "https://www.google.com"})
        # leading space is added to each attribute
        self.assertEqual(node2.props_to_html(), ' class="hi-there" href="https://www.google.com"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"class": "hi-there"})
        self.assertEqual(node.to_html(), '<div class="hi-there">Hello, world!</div>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
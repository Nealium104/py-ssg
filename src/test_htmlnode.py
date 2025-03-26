import unittest
from htmlnode import HTMLNode

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
        self.assertEqual(node2.props_to_html(), 'class="hi-there" href="https://www.google.com"')

if __name__ == "__main__":
    unittest.main()
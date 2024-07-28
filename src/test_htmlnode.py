import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        html_node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        props = html_node.props_to_html()
        self.assertEqual(props, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        html_node = HTMLNode("a", "Click Here!", None, {"href": "https://google.com", "class": "link button", "id": "external-link-5"})
        expected = "Tag: a Value: Click Here! Children: None Props: {'href': 'https://google.com', 'class': 'link button', 'id': 'external-link-5'}"
        self.assertEqual(html_node.__repr__(), expected)


if __name__ == "__main__":
    unittest.main()
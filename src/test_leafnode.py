import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

        node2 = LeafNode("h1", "This is a heading.")
        expected2 = "<h1>This is a heading.</h1>"
        self.assertEqual(node2.to_html(), expected2)

    def test_tag_and_values_with_props(self):
        node = LeafNode("a", "Click Here!", None, {"href": "https://google.com", "class": "link"})
        expected = '<a href="https://google.com" class="link">Click Here!</a>'
        self.assertEqual(node.to_html(), expected)
        
if __name__ == "__main__":
    unittest.main()
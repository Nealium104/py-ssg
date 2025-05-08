import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_url_not_none(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a link node", TextType.LINK, None)
        self.assertNotEqual(node, node2)
    
    def test_diff_nodes(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.google.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "link")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {'href': "https://www.google.com"})

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_double_bold(self):
        node = TextNode("This is text with **two** bolded **words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
                TextNode(" bolded ", TextType.TEXT),
                TextNode("words", TextType.BOLD)
            ],
            new_nodes
        )
    
    def test_bold_multi_word(self):
        node = TextNode("This is text with **two connected** and bolded words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("two connected", TextType.BOLD),
                TextNode(" and bolded words", TextType.TEXT)
            ],
            new_nodes
        )

    def test_italic(self):
        node = TextNode("This is _italicized_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_italic_multi_word(self):
        node = TextNode("This is _multi-word, italicized_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("multi-word, italicized", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_italic_and_bold(self):
        node = TextNode("This is _italicized text_ and **bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italicized text", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD)
            ],
            new_nodes
        )

    def test_code(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://google.com)"
        )
        self.assertListEqual([("image", "https://google.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://google.com)")
        self.assertListEqual([("link", "https://google.com")], matches)

if __name__ == "__main__":
    unittest.main()
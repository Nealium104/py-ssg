class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        # return true if all properties of two TextNode objects are equal
        if(self.text == node.text and self.text_type == node.text_type and self.url == node.url):
            return True
        else:
            return False

    def __repr__(self):
        # return a string of the TextNode object. it should look like this: TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
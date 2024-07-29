from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, children = None, props = None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string
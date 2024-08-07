from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("No tags present")
        if not self.children:
            raise ValueError("No children present")
        strings = ""
        array = [child.to_html() for child in self.children]
        for item in array:
            strings += item
        return f"<{self.tag}>" + strings + f"</{self.tag}>"
from textnode import TextType

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'HTMLNode(Tag:{self.tag}, Value:{self.value}, Children:{self.children}, Props:{self.props})'
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        attribute_string = ""
        if self.props is None:
            return attribute_string
        for key, value in self.props.items():
            attribute_string += f' {key}="{value}"'
        return attribute_string
    
    def text_node_to_html_node(text_node):
        if not isinstance(text_node.text_type, TextType):
            raise Exception("text_node.text_type must be an instance of TextType")
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode(None, text_node.BOLD)
        if text_node.text_type == TextType.ITALIC:
            return HTMLNode(None, text_node.italic)
        if text_node.text_type == TextType.CODE:
            return HTMLNode(None, text_node.code)
        if text_node.text_type == TextType.LINK:
            return HTMLNode(None, text_node.link)
        if text_node.text_type == TextType.IMAGE:
            return HTMLNode(None, text_node.image)
 
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f'LeafNode(Tag:{self.tag}, Value:{self.value}, Props:{self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
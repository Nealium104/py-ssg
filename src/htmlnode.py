class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        # Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
        string = ""
        for key, value in self.props.items():
           string += f' {key}="{value}"'
        return string

    def __repr__(self):
        return f'Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}'
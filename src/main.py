from textnode import TextNode

def main():
    # create a TextNode object with some dummy values. Print it. You'll move this to main.py
    node = TextNode("I'm a node", "txt", "bigdum.com")
    other_node = TextNode("I'm a node", "txt", "bigdm.com")
    print(node.__repr__())
    print(node.__eq__(other_node))

main()
from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type not in TextType:
        with Exception as e:
            raise f"Somehow {text_node} is not a valid TextType: {e}"
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, f"{text_node.text}")
        
        case TextType.BOLD:
            return LeafNode("b", f"{text_node.text}")

        case TextType.ITALIC:
            return LeafNode("i", f"{text_node.text}")
        
        case TextType.CODE:
            return LeafNode("code", f"{text_node.text}")
        
        case TextType.LINK:
            return LeafNode("link", f"{text_node.text}", text_node.url)
        
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":f"{text_node.url}", "alt":f"{text_node.text}"})
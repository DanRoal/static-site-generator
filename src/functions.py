from textnode import TextNode, TextType
from htmlnode import LeafNode
import re

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
        
def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
    res= []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            res.append(node)
            continue
        splited = node.text.split(delimiter)
        if len(splited)%2 != 1:
            raise Exception("No closing delimiter found")

        for i, text in enumerate(splited):
            if text == "":
                continue
            if i%2 == 0:
                res.append(TextNode(text, TextType.TEXT))
            else:
                res.append(TextNode(text, text_type))
    return res

def split_nodes_image(old_nodes:list[TextNode]):
    res= []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            res.append(node)
            continue
        images = extract_markdown_images(node.text)
        splited = [node.text]
        for alt, img_link in images:
            splited.extend(splited.pop(-1).split(f"![{alt}]({img_link})",1))
        index = 0
        while index < len(images):
            if splited[0] != "":
                res.append(TextNode(splited[0], TextType.TEXT))
            res.append(TextNode(images[index][0], TextType.IMAGE, images[index][1]))
            splited.pop(0)
            index+=1
        for remain in splited:
            if splited[0] != "":
                res.append(TextNode(remain, TextType.TEXT))
    return res

def split_nodes_links(old_nodes:list[TextNode]):
    res= []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            res.append(node)
            continue
        links = extract_markdown_links(node.text)
        splited = [node.text]
        for alt, link in links:
            splited.extend(splited.pop(-1).split(f"[{alt}]({link})",1))
        index = 0
        while index < len(links):
            if splited[0] != "":
                res.append(TextNode(splited[0], TextType.TEXT))
            res.append(TextNode(links[index][0], TextType.LINK, links[index][1]))
            splited.pop(0)
            index+=1
        for remain in splited:
            if splited[0] != "":
                res.append(TextNode(remain, TextType.TEXT))
    return res

def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return links


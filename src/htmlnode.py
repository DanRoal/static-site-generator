class HTMLNode:
    def __init__(self, tag:str = None, value:str = None, children:list = None, props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        formated = ""
        if self.props == None:
            return formated
        for key, val in self.props.items():
            formated += f' {key}="{val}"'
        return formated
    
    def __repr__(self):
        return f"HTMLNode: {self.__dict__}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        self.__dict__.pop("children")
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        res = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return res
    
    def __repr__(self):
        return f"LeafNode: {self.__dict__}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        self.__dict__.pop("value")
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None:
            raise ValueError("No children")
        branches = [i.to_html() for i in self.children]
        res = f"<{self.tag}{self.props_to_html()}>{"".join(branches)}</{self.tag}>"
        return res
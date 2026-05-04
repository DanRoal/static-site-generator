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
        for key, val in self.props.items():
            formated += f' {key}="{val}"'
        return formated.strip()
    
    def __repr__(self):
        return f"HTMLNode: {self.__dict__}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
class LeafNode(HTMLNode):
    pass
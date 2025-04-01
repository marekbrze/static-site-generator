class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""
        if self.props:
            for key in self.props:
                props_string += f'{key}="{self.props[key]}" '
        return props_string.strip()

    def __repr__(self):
        repr_string = "HTML NODE:\n"
        if self.tag:
            repr_string += f"tag: {self.tag}\n"
        if self.value:
            repr_string += f"value: {self.value}\n"
        if self.children:
            repr_string += f"children: {self.children}\n"
        if self.props:
            repr_string += f"props: {self.props}\n"
        return repr_string.strip()

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf needs to have a value")
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None and self.children == None:
            raise ValueError("You need to specify tag and children!")
        if self.tag == None:
            raise ValueError("You need to specify tag!")
        if self.children == None:
            raise ValueError("You need to specify children!")

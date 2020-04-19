from Nodes.Symbols import variables

# variable node
class Node:

    def __init__(self,name):
        self.name = name

    def visit(self):
        value = variables.get(self.name)
        return value

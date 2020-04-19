# variable node
class Node:

    def __init__(self,name):
        self.name = name

    def visit(self):
        value = variables.get(self.name,None)
        if not value:
            return 0
        else:
            return value

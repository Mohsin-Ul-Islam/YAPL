# literal node
class Node:

    def __init__(self,value):
        self.value = value

    def visit(self,context=None):
        return self.value

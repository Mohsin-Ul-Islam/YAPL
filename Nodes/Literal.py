# literal node
class Node:

    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def visit(self):
        return self.value

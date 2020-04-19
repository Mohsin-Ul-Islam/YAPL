# factor node
class Node:

    def __init__(self,child):
        self.child = child

    def visit(self):
        return self.child.visit()

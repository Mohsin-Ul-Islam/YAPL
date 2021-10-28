# factor node
class Node:
    def __init__(self, child):
        self.child = child

    def visit(self, context):
        return self.child.visit(context)

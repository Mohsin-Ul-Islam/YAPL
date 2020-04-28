# term node
class Node:

    def __init__(self,left,op = None,right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self,context):
        if not self.op:
            return self.left.visit(context)
        elif self.op == '*':
            return self.left.visit(context) * self.right.visit(context)
        elif self.op == '/':
            return self.left.visit(context) / self.right.visit(context)

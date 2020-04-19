# term node
class Node:

    def __init__(self,left,op = None,right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self):
        if not self.op:
            return self.left.visit()
        elif self.op == '*':
            return self.left.visit() * self.right.visit()
        elif self.op == '/':
            return self.left.visit() / self.right.visit()

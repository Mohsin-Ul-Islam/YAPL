class Node:

    def __init__(self,expression):
        self.expression = expression

    def visit(self):
        return self.expression.visit()

class Node:
    def __init__(self, expression):
        self.expression = expression

    def visit(self, context):
        return self.expression.visit(context)

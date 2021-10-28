class Node:
    def __init__(self, condition, body, otherwise=None):
        self.condition = condition
        self.body = body
        self.otherwise = otherwise

    def visit(self, context=None):
        if self.condition.visit(context):
            return self.body.visit(context)
        elif self.otherwise:
            return self.otherwise.visit(context)

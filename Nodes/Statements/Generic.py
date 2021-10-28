class Node:
    def __init__(self, statement):
        self.statement = statement

    def visit(self, context):
        return self.statement.visit(context)

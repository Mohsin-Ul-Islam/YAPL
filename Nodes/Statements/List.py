class Node:
    def __init__(self, statement=None, list=None):
        self.statement = statement
        self.list = list

    def visit(self, context):
        rvalue = None
        if self.statement:
            rvalue = self.statement.visit(context)
        if self.list:
            rvalue = self.list.visit(context)
        return rvalue

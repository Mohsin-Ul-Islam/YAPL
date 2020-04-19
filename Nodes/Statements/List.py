class Node:

    def __init__(self,statement = None, list = None):
        self.statement = statement
        self.list      = list

    def visit(self):
        rvalue = None
        if self.statement:
            rvalue = self.statement.visit()
        if self.list:
            rvalue = self.list.visit()
        return rvalue

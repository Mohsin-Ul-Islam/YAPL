class Node:

    def __init__(self,name,body,arguments=None):
        self.name      = name
        self.arguments = arguments
        self.body      = body

    def visit(self,context=None):
        return self.body.visit(context)

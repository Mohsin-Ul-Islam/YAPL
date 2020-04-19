class Node:

    def __init__(self,name,body,arguments=None):
        self.name      = name
        self.arguments = arguments
        self.body      = body

    def visit(self,args=None):
        return self.body.visit()

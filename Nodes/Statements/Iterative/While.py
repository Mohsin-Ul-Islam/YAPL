class Node:

    def __init__(self,condition,body):

        self.condition = condition
        self.body      = body

    def visit(self,context):
        rvalue = None
        while(self.condition.visit(context)):
            rvalue = self.body.visit(context)
        return rvalue

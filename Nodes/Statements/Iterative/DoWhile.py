class Node:

    def __init__(self,condition,body):
        self.condition = condition
        self.body      = body

    def visit(self):
        rvalue = self.body.visit()
        while self.condition.visit():
            rvalue = self.body.visit()

class Node:

    def __init__(self,condition,body,otherwise = None):
        self.condition = condition
        self.body      = body
        self.otherwise = otherwise

    def visit(self):
        if self.condition.visit():
            return self.body.visit()
        elif self.otherwise:
            return self.otherwise.visit()

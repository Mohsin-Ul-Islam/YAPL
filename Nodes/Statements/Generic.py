class Node:

    def __init__(self,statement):
        self.statement = statement

    def visit(self):
        return self.statement.visit()

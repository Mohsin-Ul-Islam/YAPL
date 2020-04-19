from Nodes.Symbols import variables

class Node:

    def __init__(self,name,expression):

        self.name       = name
        self.expression = expression

    def visit(self):

        global variables
        variables[self.name] = self.expression.visit()
        return variables[self.name]

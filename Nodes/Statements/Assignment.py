from Nodes.Symbols import variables

class Node:

    def __init__(self,name,op,expression):

        self.name       = name
        self.expression = expression
        self.op         = op

    def visit(self):

        if self.op == '=':
            variables.set(self.name,self.expression.visit())
        elif self.op == 'declare':
            variables.declare(self.name,self.expression.visit())
        elif self.op == '+=':
            variables.set(self.name,variables.get(self.name) + self.expression.visit())
        elif self.op == '-=':
            variables.set(self.name,variables.get(self.name) - self.expression.visit())
        elif self.op == '*=':
            variables.set(self.name,variables.get(self.name) * self.expression.visit())
        elif self.op == '/=':
            variables.set(self.name,variables.get(self.name) / self.expression.visit())

        return variables.get(self.name)

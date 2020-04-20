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
        elif self.op == 'int' or self.op == 'double' or self.op == 'string' or self.op == 'char' or self.op == 'bool':
            variables.declareStrict(self.name,self.expression.visit(),self.op)
        elif self.op == '+=':
            variables.set(self.name,variables.get(self.name) + self.expression.visit())
        elif self.op == '-=':
            variables.set(self.name,variables.get(self.name) - self.expression.visit())
        elif self.op == '*=':
            variables.set(self.name,variables.get(self.name) * self.expression.visit())
        elif self.op == '/=':
            variables.set(self.name,variables.get(self.name) / self.expression.visit())

        return variables.get(self.name)

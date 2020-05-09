from State.SymbolTable import table

class Node:

    def __init__(self,name,op,expression):

        self.name       = name
        self.expression = expression
        self.op         = op

    def visit(self,context):

        if self.op == '=':
            table.setVariable(self.name,self.expression.visit(context))
        elif self.op == '+=':
            table.setVariable(self.name,table.getVariable(self.name) + self.expression.visit(context))
        elif self.op == '-=':
            table.setVariable(self.name,table.getVariable(self.name) - self.expression.visit(context))
        elif self.op == '*=':
            table.setVariable(self.name,table.getVariable(self.name) * self.expression.visit(context))
        elif self.op == '/=':
            table.setVariable(self.name,table.getVariable(self.name) / self.expression.visit(context))
        elif self.op == '%=':
            table.setVariable(self.name,table.getVariable(self.name) % self.expression.visit(context))

        return table.getVariable(self.name)

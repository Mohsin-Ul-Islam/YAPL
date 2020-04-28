from Errors import VariableTypeError
# expressions node
from State.SymbolTable import table

class Node:

    def __init__(self, left, op = None, right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self,context):

        if not self.op:
            return self.left.visit(context)

        elif self.op == '^':
            return self.left.visit(context) ** self.right.visit(context)

        elif self.op == '!=':
            return self.left.visit(context) != self.right.visit(context)

        elif self.op == '!':
            return not self.left.visit(context)

        elif self.op == '-' and not self.right:
            return -self.left.visit(context)

        elif self.op == '++':
            table.setVariable(self.left,table.getVariable(self.left) + 1)
            return table.getVariable(self.left)

        elif self.op == '--':
            table.setVariable(self.left,table.getVariable(self.left) - 1)
            return table.getVariable(self.left)

        # handles implicit string conversions during addition
        elif self.op == '+':
            left  = self.left.visit(context)
            right = self.right.visit(context)
            if (type(left) == str and type(right) != str) or (type(right) == str and type(left) != str):
                raise VariableTypeError("TypeError: Cannot convert string")
            return self.left.visit(context) + self.right.visit(context)

        elif self.op == '-':
            return self.left.visit(context) - self.right.visit(context)

        elif self.op == '&&':
            return self.left.visit(context) and self.right.visit(context)

        elif self.op == '||':
            return self.left.visit(context) or self.right.visit(context)

        elif self.op == '==':
            return self.left.visit(context) == self.right.visit(context)

        elif self.op == '<=':
            return self.left.visit(context) <= self.right.visit(context)

        elif self.op == '>=':
            return self.left.visit(context) >= self.right.visit(context)

        elif self.op == '<':
            return self.left.visit(context) < self.right.visit(context)

        elif self.op == '>':
            return self.left.visit(context) > self.right.visit(context)

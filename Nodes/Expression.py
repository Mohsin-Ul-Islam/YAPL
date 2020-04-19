# expressions node

class Node:

    def __init__(self, left, op = None, right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self):

        if not self.op:
            return self.left.visit()

        elif self.op == '!':
            return not self.left.visit()

        elif self.op == '-' and not self.right:
            return -self.left.visit()

        # handles implicit string conversions during addition
        elif self.op == '+':
            left  = self.left.visit()
            right = self.right.visit()
            if type(left) == str or type(right) == str:
                return str(left) + str(right)
            return self.left.visit() + self.right.visit()

        elif self.op == '-':
            return self.left.visit() - self.right.visit()

        elif self.op == '&&':
            return self.left.visit() and self.right.visit()

        elif self.op == '||':
            return self.left.visit() or self.right.visit()

        elif self.op == '==':
            return self.left.visit() == self.right.visit()

        elif self.op == '<=':
            return self.left.visit() <= self.right.visit()

        elif self.op == '>=':
            return self.left.visit() >= self.right.visit()

        elif self.op == '<':
            return self.left.visit() < self.right.visit()

        elif self.op == '>':
            return self.left.visit() > self.right.visit()

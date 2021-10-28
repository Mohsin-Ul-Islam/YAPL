class Node:
    def __init__(self, arg, list=None):
        self.arg = arg
        self.list = list

    def visit(self, context=None):
        rvalue = []
        if self.arg:
            rvalue = rvalue + [self.arg.visit(context)]
        if self.list:
            rvalue = rvalue + self.list.visit(context)
        return rvalue

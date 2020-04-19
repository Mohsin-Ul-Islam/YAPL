class Node:

    def __init__(self,arg,list = None):
        self.arg  = arg
        self.list = list

    def visit(self):
        rvalue = []
        if self.arg:
            rvalue = rvalue + [self.arg.visit()]
        if self.list:
            rvalue = rvalue + self.list.visit()
        return rvalue

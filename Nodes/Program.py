class Node:

    def __init__(self,declaration_list):
        self.declaration_list = declaration_list

    def visit(self):
        context = {'type':'program'}
        return self.declaration_list.visit(context)

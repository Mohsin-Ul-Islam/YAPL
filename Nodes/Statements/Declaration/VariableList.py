class Node:

    def __init__(self,variable_declaration,list):

        self.variable_declaration = variable_declaration
        self.list                 = list
        
    def visit(self,context):

        rvalue1 = self.variable_declaration.visit(context)
        rvalue2 = self.list.visit(context)

        if rvalue2:
            return rvalue2
        else:
            return rvalue1

class Node:

    def __init__(self,statement,list):

        self.statement = statement
        self.list      = list

    def visit(self,context):

        rvalue1 = self.statement.visit(context)
        rvalue2 = self.list.visit(context)

        if rvalue2:
            return rvalue2
        else:
            return rvalue1

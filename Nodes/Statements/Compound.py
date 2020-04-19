from Nodes.Symbols import variables

class Node:

    def __init__(self,statement_list):
        self.statement_list = statement_list

    def visit(self):
        variables.push()
        rvalue = self.statement_list.visit()
        variables.pop()
        return rvalue

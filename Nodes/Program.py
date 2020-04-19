class Node:

    def __init__(self,statement_list):
        self.statement_list = statement_list

    def visit(self):
        return self.statement_list.visit()

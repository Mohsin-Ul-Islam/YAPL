from State.SymbolTable import table


class Node:
    def __init__(self, statement_list):
        self.statement_list = statement_list

    def visit(self, context):
        table.push()
        rvalue = self.statement_list.visit(context)
        table.pop()
        return rvalue

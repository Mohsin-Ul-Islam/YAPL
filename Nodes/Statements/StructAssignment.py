from State.SymbolTable import table

class Node:

    def __init__(self,struct_name,member_name,expression):

        self.struct_name = struct_name
        self.member_name = member_name
        self.expression  = expression

    def visit(self,context):
        rvalue = self.expression.visit(context)
        table.setStructMember(self.struct_name,self.member_name,rvalue)
        return rvalue

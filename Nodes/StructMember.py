from State.SymbolTable import table


class Node:
    def __init__(self, struct_name, member_name):

        self.struct_name = struct_name
        self.member_name = member_name

    def visit(self, context):
        return table.getStructMember(self.struct_name, self.member_name)

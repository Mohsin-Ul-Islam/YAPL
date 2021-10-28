from State.SymbolTable import table

# variable node
class Node:
    def __init__(self, name):
        self.name = name

    def visit(self, context):
        if context["type"] == "program":
            value = table.getVariable(self.name)
            return value
        elif context["type"] == "struct":
            value = table.getStructMember(context["name"], self.name)
            return value

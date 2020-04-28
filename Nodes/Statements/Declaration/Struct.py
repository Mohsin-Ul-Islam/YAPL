from State.SymbolTable import table

class Node:

    def __init__(self,name,list):

        self.name = name
        self.list = list

    def visit(self,context):
        context = {"type":"struct","name":self.name}
        table.newStruct(self.name)
        return self.list.visit(context)
        

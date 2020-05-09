from State.SymbolTable import table

class Node:

    def __init__(self,struct_name,instance_name):

        self.struct_name = struct_name
        self.instance_name = instance_name

    def visit(self,context):

        table.insertStruct(self.struct_name,self.instance_name)

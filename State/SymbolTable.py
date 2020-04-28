from State.Variable  import Variable
from State.Structure import Struct
from Errors import *

class SymbolTable:

    def __init__(self):
        self.variables = {}
        self.structs   = {}
        self.index     = -1
        self.push()

    def insertVariable(self,name,value=None,specifier=None):
        s = self.scope(name)
        if s != self.index:
            self.variables[self.index][name] = Variable(name,value,specifier)
            return value
        else:
            raise RedeclarationError("RedeclarationError\nVariable: " + str(name) + " already defined.")

    def setVariable(self,name,value):
        s = self.scope(name)
        if s == -1:
            raise VariableNotDefinedError("VariableNotDefinedError\nUndefined Variable: " + str(name))
        else:
            variable = self.variables.get(s).get(name,None)
            if variable:
                self.variables[s][name].setValue(value)
            else:
                raise VariableTypeError("Cannot assign struct variable a value.")
        return value

    def getVariable(self,name):
        s = self.scope(name)
        if s == -1:
            raise VariableNotDefinedError("VariableNotDefinedError\nUndefined Variable: " + str(name))
        else:
            return self.variables.get(s).get(name).getValue()

    #structure methods
    def newStruct(self,struct_name,member_name=None,value=None,specifier=None):
        s = self.scope(struct_name)
        if s != self.index:
            self.structs[self.index][struct_name] = Struct(struct_name,member_name,value,specifier)
            return value
        else:
            raise RedeclarationError("RedeclarationError\nStruct: " + str(struct_name) + " already defined.")

    def insertStruct(self,struct_name,member_name,value=None,specifier=None):
        self.structs[self.index][struct_name].addMember(member_name,value,specifier)

    def getStructMember(self,struct_name,member_name):
        s = self.scope(struct_name)
        if s == -1:
            raise VariableNotDefinedError("StructNotDefined\nUndefined Struct: " + str(name))
        else:
            return self.structs.get(s).get(struct_name).getMember(member_name)

    def setStructMember(self,struct_name,member_name,value):
        s = self.scope(struct_name)
        if s == -1:
            raise VariableNotDefinedError("Struct Not defined Error")
        else:
            self.structs[s][struct_name].setMember(member_name,value)



    def push(self):
        self.index += 1
        self.variables[self.index] = {}
        self.structs[self.index] = {}

    def pop(self):
        del self.variables[self.index]
        del self.structs[self.index]
        self.index -= 1

    def scope(self,name):
        for scope in range(self.index,-1,-1):
            if self.variables.get(scope).get(name,None) or self.structs.get(scope).get(name,None):
                return scope
        return -1

table = SymbolTable()

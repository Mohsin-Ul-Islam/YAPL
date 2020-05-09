import copy
from State.Variable  import Variable
from State.Structure import Struct
from Errors import *

class SymbolTable:

    def __init__(self):
        self.variables = {}
        self.structs   = {}
        self.functions = {}
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
        if self.structs.get(struct_name,None):
            raise RedeclarationError("RedeclarationError\nStruct: " + str(struct_name) + " already defined.")
        else:
            self.structs[struct_name] = Struct(struct_name,member_name,value,specifier)
            return value

    def insertStructMember(self,struct_name,member_name,value=None,specifier=None):
        if self.structs.get(struct_name,None):
            if self.structs.get(member_name,None):
                raise RedeclarationError("RedeclarationError\n Struct member already defined.")
            else:
                self.structs[struct_name].addMember(member_name,value,specifier)
        else:
            raise VariableNotDefinedError("UndeclaredStructError\n")

    def insertStruct(self,struct_name,instance_name):
        s = self.scope(instance_name)
        if self.structs.get(struct_name,None):
            if s != self.index:
                self.variables[self.index][instance_name] = copy.deepcopy(self.structs[struct_name])
            else:
                raise RedeclarationError("RedeclarationError\nVariable: " + str(instance_name) + " already defined.")
        else:
            raise VariableNotDefinedError("StructNotDefinedError\nUndefined Struct: " + str(struct_name))


    def getStructMember(self,struct_name,member_name):
        s = self.scope(struct_name)
        if s == -1:
            raise VariableNotDefinedError("StructNotDefined\nUndefined Struct: " + str(struct_name))
        else:
            return self.variables.get(s).get(struct_name).getMember(member_name)

    def setStructMember(self,struct_name,member_name,value):
        s = self.scope(struct_name)
        if s == -1:
            raise VariableNotDefinedError("Struct Not defined Error")
        else:
            self.variables[s][struct_name].setMember(member_name,value)



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
            if self.variables.get(scope).get(name,None):
                return scope
        return -1

table = SymbolTable()

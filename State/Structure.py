from State.Variable import Variable
from Errors import *

class Struct:

    def __init__(self,struct_name,member_name=None,value=None,specifier=None):

        self.struct_name = struct_name
        self.struct      = {}

        if member_name:
            self.addMember(member_name,value,specifier)

    def addMember(self,member_name,value,specifier):
        self.struct[member_name] = Variable(member_name,value,specifier)

    def getMember(self,member_name):
        member = self.struct.get(member_name,None)
        if member:
            return self.struct[member_name].getValue()
        else:
            raise VariableNotDefinedError("Undefined Struct Member: " + str(member_name))

    def setMember(self,member_name,value):
        member = self.struct.get(member_name,None)
        if member:
            self.struct[member_name].setValue(value)
            return value
        else:
            raise VariableNotDefinedError("Undefined Struct Member: " + str(member_name))

from Errors import *


class Variable:
    def __init__(self, name, value=None, specifier=None):

        self.name = name
        self.specifier = specifier
        self.value = ""
        self.setValue(value)

    def getValue(self):
        return self.value

    def getSpecifier(self):
        return self.specifier

    def getName(self):
        return self.name

    def setValue(self, value):
        if not value:
            self.value = self.getDefault()
        elif self.isValidType(value):
            self.value = value
        else:
            raise VariableTypeError("TypeError: Mismatch type")

    def getDefault(self):
        if self.specifier == "int":
            return 0
        elif self.specifier == "double":
            return 0.0
        elif self.specifier == "char" or self.specifier == "string":
            return ""
        elif self.specifier == "bool":
            return "false"

    def isValidType(self, value):
        if not self.specifier:
            return True
        if self.specifier == "int" and isinstance(value, int):
            return True
        elif self.specifier == "double" and isinstance(value, float):
            return True
        elif self.specifier == "char" and isinstance(value, str):
            return True
        elif self.specifier == "string" and isinstance(value, str):
            return True
        elif self.specifier == "bool" and (value == "true" or value == "false"):
            return True
        else:
            return False

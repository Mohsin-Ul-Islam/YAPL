class Variable:

    def __init__(self,value,specifier=None):

        self.value = value
        self.specifier = specifier

    def value(self):
        return self.value

    def specifier(self):
        return self.specifier

class Scope:

    def __init__(self):

        self.scope_level = 0
        self.table       = {}
        self.table[self.scope_level] = {}

    def present(self,name,scope):
        if not self.table.get(scope).get(name,None):
            return False
        else:
            return True

    def checkType(self,specifier,value):
        if((specifier == 'int' and type(value) == int) or (specifier == 'double' and type(value) == float) or (specifier == 'string' and type(value) == str) or (specifier == 'char' and type(value) == str and len(value) == 1) or (specifier == 'bool' and (value == 'true' or value == 'false'))):
            return True
        else:
            return False

    def push(self):
        self.scope_level += 1
        self.table[self.scope_level] = {}

    def pop(self):

        del self.table[self.scope_level]
        self.scope_level -= 1

    def get(self,name):
        rvalue = None
        for scope_level in range(self.scope_level,-1,-1):
            rvalue = self.table.get(scope_level).get(name,None)
            if rvalue:
                return rvalue.value
        raise NameError

    def set(self,name,value):
        rvalue = None
        for scope_level in range(self.scope_level,-1,-1):
            if self.present(name,scope_level):
                if self.table[scope_level][name].specifier:
                    if self.checkType(self.table[scope_level][name].specifier,value):
                        self.table[scope_level][name].value = value
                        return value
                    else:
                        raise TypeError
                else:
                    self.table[scope_level][name].value = value
                    return value
        raise NameError

    def declare(self,name,value):

        if not self.present(name,self.scope_level):
            self.table[self.scope_level][name] = Variable(value)
        #print(self.table)
        else:
            raise NameError

    def declareStrict(self,name,value,specifier):

        if not self.present(name,self.scope_level):
            if self.checkType(specifier,value):
                self.table[self.scope_level][name] = Variable(value,specifier)
            else:
                raise TypeError
        else:
            raise NameError

variables = Scope()

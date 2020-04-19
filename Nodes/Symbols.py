class Scope:

    def __init__(self):

        self.scope_level = 0
        self.table       = {}
        self.table[self.scope_level] = {}

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
                return rvalue
        raise NameError

    def set(self,name,value):
        rvalue = None
        for scope_level in range(self.scope_level,-1,-1):
            if self.table.get(scope_level).get(name,None):
                self.table[scope_level][name] = value
                return value
        raise NameError

    def declare(self,name,value):

        if not self.table.get(self.scope_level).get(name,None):
            self.table[self.scope_level][name] = value
        #print(self.table)
        else:
            raise NameError

variables = Scope()

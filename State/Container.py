class ProgramContainer:
    def __init__(self, table, scope):
        self.table = table
        self.scope = scope

    def InBlock(self):
        self.scope.push()
        self.table.addScope(self.scope.level)

    def OutBlock(self):
        self.table.removeScope(self.scope.level)
        self.scope.pop()

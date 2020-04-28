class Node:

    def __init__(self,name,arguments = None):
        self.name      = name
        self.arguments = arguments

    def visit(self,context=None):
        if not routines[self.name]:
            return False
        elif self.arguments:
            args = self.arguments.visit(context)
            return routines[self.name].visit(args)
        else:
            return routines[self.name].visit(context)

class Node:

    def __init__(self,arguments):
        self.arguments = arguments

    def visit(self):
        result = ''
        for arg in self.arguments.visit():
            result += str(arg)
        print(result)
        return True

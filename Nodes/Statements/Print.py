class Node:
    def __init__(self, arguments):
        self.arguments = arguments

    def visit(self, context):
        result = ""
        for arg in self.arguments.visit(context):
            result += str(arg) + " "
        result = result[:-1]
        print(result)
        return

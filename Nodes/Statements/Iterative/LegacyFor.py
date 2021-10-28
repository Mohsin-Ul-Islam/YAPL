class Node:
    def __init__(self, initialization, condition, increment, body):

        self.initialization = initialization
        self.condition = condition
        self.increment = increment
        self.body = body

    def visit(self, context):
        rvalue = None
        self.initialization.visit(context)
        while self.condition.visit(context):
            rvalue = self.body.visit(context)
            self.increment.visit(context)
        return rvalue

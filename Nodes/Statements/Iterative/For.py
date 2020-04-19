class Node:

    def __init__(self,start,end,body,step=None):
        self.start = start
        self.end   = end
        self.body  = body
        self.step  = step

    def visit(self):
        rvalue = None
        if not self.step:
            for i in range(self.start.visit(),self.end.visit()):
                rvalue = self.body.visit()
        else:
            for i in range(self.start.visit(),self.end.visit(),self.step.visit()):
                rvalue = self.body.visit()

        return rvalue

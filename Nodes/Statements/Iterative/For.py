class Node:

    def __init__(self,start,end,body,step=None):
        self.start = start
        self.end   = end
        self.body  = body
        self.step  = step

    def visit(self,context):
        rvalue = None
        if not self.step:
            for i in range(self.start.visit(context),self.end.visit(context)):
                rvalue = self.body.visit(context)
        else:
            for i in range(self.start.visit(context),self.end.visit(context),self.step.visit(context)):
                rvalue = self.body.visit(context)
        return rvalue

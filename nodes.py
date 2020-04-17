variables = {}
routines  = {}

class AST:
    pass

# literal node
class LiteralNode(AST):

    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def visit(self):
        return self.value

# variable node
class IdentifierNode(AST):

    def __init__(self,name):
        self.name = name

    def visit(self):
        value = variables.get(self.name,None)
        if not value:
            return 0
        else:
            return value

# factor node
class FactorNode(AST):

    def __init__(self,child):
        self.child = child

    def visit(self):
        return self.child.visit()

# term node
class TermNode(AST):

    def __init__(self,left,op = None,right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self):
        if not self.op:
            return self.left.visit()
        elif self.op == '*':
            return self.left.visit() * self.right.visit()
        elif self.op == '/':
            return self.left.visit() / self.right.visit()

class ExpressionNode(AST):

    def __init__(self, left, op = None, right = None):
        self.left  = left
        self.op    = op
        self.right = right

    def visit(self):

        if not self.op:
            return self.left.visit()

        elif self.op == '!':
            return not self.left.visit()

        elif self.op == '-' and not self.right:
            return -self.left.visit()

        # handles implicit string conversions during addition
        elif self.op == '+':
            left  = self.left.visit()
            right = self.right.visit()
            if type(left) == str or type(right) == str:
                return str(left) + str(right)
            return self.left.visit() + self.right.visit()

        elif self.op == '-':
            return self.left.visit() - self.right.visit()

        elif self.op == '&&':
            return self.left.visit() and self.right.visit()

        elif self.op == '||':
            return self.left.visit() or self.right.visit()

        elif self.op == '==':
            return self.left.visit() == self.right.visit()

        elif self.op == '<=':
            return self.left.visit() <= self.right.visit()

        elif self.op == '>=':
            return self.left.visit() >= self.right.visit()

        elif self.op == '<':
            return self.left.visit() < self.right.visit()

        elif self.op == '>':
            return self.left.visit() > self.right.visit()

class AssignmentStmntNode(AST):

    def __init__(self,name,expression):

        self.name       = name
        self.expression = expression

    def visit(self):

        global variables
        variables[self.name] = self.expression.visit()
        return variables[self.name]

class PrintStmntNode(AST):

    def __init__(self,arguments):
        self.arguments = arguments

    def visit(self):
        result = ''
        for arg in self.arguments.visit():
            result += str(arg)
        print(result)
        return True

class ArgumentsNode(AST):

    def __init__(self,arg,list = None):
        self.arg  = arg
        self.list = list

    def visit(self):
        rvalue = []
        if self.arg:
            rvalue = rvalue + [self.arg.visit()]
        if self.list:
            rvalue = rvalue + self.list.visit()
        return rvalue

class ExpressionStmntNode(AST):

    def __init__(self,expression):
        self.expression = expression

    def visit(self):
        return self.expression.visit()

class IterativeWhileStmntNode(AST):

    def __init__(self,condition,body):

        self.condition = condition
        self.body      = body

    def visit(self):
        rvalue = None
        while(self.condition.visit()):
            rvalue = self.body.visit()
        return rvalue

class IterativeDoWhileStmntNode(AST):

    def __init__(self,condition,body):
        self.condition = condition
        self.body      = body

    def visit(self):
        rvalue = self.body.visit()
        while self.condition.visit():
            rvalue = self.body.visit()

class IterativeForStmntNode(AST):

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

class ConditionalStmntNode(AST):

    def __init__(self,condition,body,otherwise = None):
        self.condition = condition
        self.body      = body
        self.otherwise = otherwise

    def visit(self):
        if self.condition.visit():
            return self.body.visit()
        elif self.otherwise:
            return self.otherwise.visit()

class CompoundStmntNode(AST):

    def __init__(self,statement_list):
        self.statement_list = statement_list

    def visit(self):
        return self.statement_list.visit()

class FunctionNode(AST):

    def __init__(self,name,body,arguments=None):
        self.name      = name
        self.arguments = arguments
        self.body      = body

    def visit(self,args=None):
        return self.body.visit()

class FunctionCallStmnt(AST):

    def __init__(self,name,arguments = None):
        self.name      = name
        self.arguments = arguments

    def visit(self):
        if not routines[self.name]:
            return False
        elif self.arguments:
            args = self.arguments.visit()
            return routines[self.name].visit(args)
        else:
            return routines[self.name].visit()


class StmntListNode(AST):

    def __init__(self,statement = None, list = None):
        self.statement = statement
        self.list      = list

    def visit(self):
        rvalue = None
        if self.statement:
            rvalue = self.statement.visit()
        if self.list:
            rvalue = self.list.visit()
        return rvalue

class StmntNode(AST):

    def __init__(self,statement):
        self.statement = statement

    def visit(self):
        return self.statement.visit()

class ProgramNode(AST):

    def __init__(self,statement_list):
        self.statement_list = statement_list

    def visit(self):
        return self.statement_list.visit()

class NoOperationNode(AST):

    def __init__(self):
        pass

    def visit(self):
        pass

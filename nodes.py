variables = {}

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
        elif self.op == '+':
            return self.left.visit() + self.right.visit()
        elif self.op == '-':
            return self.left.visit() - self.right.visit()
        elif self.op == '&&':
            return self.left.visit() and self.right.visit()
        elif self.op == '||':
            return self.left.visit() or self.right.visit()
        elif self.op == '==':
            return self.left.visit() == self.right.visit()

class AssignmentStmntNode(AST):

    def __init__(self,name,expression):

        self.name       = name
        self.expression = expression

    def visit(self):

        global variables
        variables[self.name] = self.expression.visit()
        return variables[self.name]

class PrintStmntNode(AST):

    def __init__(self,expression):
        self.expression = expression

    def visit(self):
        print(self.expression.visit())
        return True

class ExpressionStmntNode(AST):

    def __init__(self,expression):
        self.expression = expression

    def visit(self):
        return self.expression.visit()

class IterativeStmntNode(AST):

    def __init__(self,condition,body):

        self.condition = condition
        self.body      = body

    def visit(self):
        rvalue = None
        while(self.condition.visit()):
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

import Nodes.Functions.Function
import Nodes.NoOperation

def p_function_statement(p):
    'function_statement : FUNCTION IDENTIFIER LEFT_PAREN arguments RIGHT_PAREN compound_statement'
    routines[p[2]] = Nodes.Functions.Function.Node(p[2],p[4],p[6])
    p[0] = Nodes.NoOperation.Node()

def p_function_statement_empty(p):
    'function_statement : FUNCTION IDENTIFIER LEFT_PAREN RIGHT_PAREN compound_statement'
    routines[p[2]] = Nodes.Functions.Function.Node(p[2],p[5])
    p[0] = Nodes.NoOperation.Node()

import Nodes.Functions.Call

def p_function_call_empty(p):
    'function_call : IDENTIFIER LEFT_PAREN RIGHT_PAREN SEMICOLON'
    p[0] = Nodes.Functions.Call.Node(p[1])

def p_function_call(p):
    'function_call : IDENTIFIER LEFT_PAREN arguments RIGHT_PAREN SEMICOLON'
    p[0] = Nodes.Functions.Call.Node(p[1],p[3])

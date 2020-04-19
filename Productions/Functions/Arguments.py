import Nodes.Functions.Arguments

def p_arguments(p):
    '''arguments   : expression COMMA arguments'''
    p[0] = Nodes.Functions.Arguments.Node(p[1],p[3])

def p_arguments_single(p):
    'arguments : expression'
    p[0] = Nodes.Functions.Arguments.Node(p[1])

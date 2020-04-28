import Nodes.NoOperation

def p_empty(p):
    'empty :'
    p[0] = Nodes.NoOperation.Node()

import Nodes.Statements.Iterative.For

def p_for_01(p):
    'iterative_statement : FOR LEFT_PAREN expression TO expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[3],p[5],p[7])

def p_for_02(p):
    'iterative_statement : FOR LEFT_PAREN expression TO expression STEP expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[3],p[5],p[9],p[7])

def p_for_03(p):
    'iterative_statement : FOR expression TO expression compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[2],p[4],p[5])

def p_for_04(p):
    'iterative_statement : FOR expression TO expression STEP expression compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[2],p[4],p[7],p[6])

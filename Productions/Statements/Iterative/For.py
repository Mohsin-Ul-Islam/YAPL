import Nodes.Statements.Iterative.For

def p_iterative_statement_for(p):
    'iterative_statement : FOR LEFT_PAREN expression TO expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[3],p[5],p[7])

def p_iterative_statement_for_step(p):
    'iterative_statement : FOR LEFT_PAREN expression TO expression STEP expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.For.Node(p[3],p[5],p[9],p[7])

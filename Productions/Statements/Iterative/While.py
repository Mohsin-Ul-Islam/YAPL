import Nodes.Statements.Iterative.While


def p_while_strict(p):
    "iterative_statement : WHILE LEFT_PAREN expression RIGHT_PAREN compound_statement"
    p[0] = Nodes.Statements.Iterative.While.Node(p[3], p[5])


def p_while(p):
    "iterative_statement : WHILE expression compound_statement"
    p[0] = Nodes.Statements.Iterative.While.Node(p[2], p[3])

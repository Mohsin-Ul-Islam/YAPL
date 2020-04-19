import Nodes.Statements.Iterative.DoWhile

def p_iterative_statement_do_while(p):
    'iterative_statement : DO compound_statement WHILE LEFT_PAREN expression RIGHT_PAREN'
    p[0] = Nodes.Statements.Iterative.DoWhile.Node(p[5],p[2])

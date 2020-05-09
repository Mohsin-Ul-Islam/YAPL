import Nodes.Statements.Iterative.DoWhile

def p_do_while_01(p):
    'iterative_statement : DO compound_statement WHILE LEFT_PAREN expression RIGHT_PAREN'
    p[0] = Nodes.Statements.Iterative.DoWhile.Node(p[5],p[2])

def p_do_while_02(p):
    'iterative_statement : DO compound_statement WHILE LEFT_PAREN expression RIGHT_PAREN SEMICOLON'
    p[0] = Nodes.Statements.Iterative.DoWhile.Node(p[5],p[2])

def p_do_while_03(p):
    'iterative_statement : DO compound_statement WHILE expression'
    p[0] = Nodes.Statements.Iterative.DoWhile.Node(p[4],p[2])

def p_do_while_04(p):
    'iterative_statement : DO compound_statement WHILE expression SEMICOLON'
    p[0] = Nodes.Statements.Iterative.DoWhile.Node(p[4],p[2])

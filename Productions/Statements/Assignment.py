import Nodes.Statements.Assignment

def p_statement_descriptive(p):
    'assignment_statement : PUT expression IN IDENTIFIER SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[4],p[2])

def p_statement_assignment(p):
    'assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[1],p[3])

def p_statement_assignment_let(p):
    'assignment_statement : LET IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[2],p[4])

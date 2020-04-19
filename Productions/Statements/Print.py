import Nodes.Statements.Print

def p_statement_log(p):
    'print_statement : LOG LEFT_PAREN arguments RIGHT_PAREN SEMICOLON'
    p[0] = Nodes.Statements.Print.Node(p[3])

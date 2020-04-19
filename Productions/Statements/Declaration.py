import Nodes.Statements.Assignment

def p_statement_declaration(p):
    'declaration_statement : type_specifier IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[2],p[4])

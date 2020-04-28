import Nodes.Statements.Declaration.Variable

def p_declaration_01(p):
    'variable_declaration : LET IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Declaration.Variable.Node(p[2],p[4])

def p_declaration_02(p):
    'variable_declaration : type_specifier IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Declaration.Variable.Node(p[2],p[4],p[1])

def p_declaration_03(p):
    'variable_declaration : type_specifier IDENTIFIER SEMICOLON'
    p[0] = Nodes.Statements.Declaration.Variable.Node(p[2],None,p[1])

def p_declaration_04(p):
    'variable_declaration : LET IDENTIFIER SEMICOLON'
    p[0] = Nodes.Statements.Declaration.Variable.Node(p[2])

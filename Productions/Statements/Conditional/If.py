import Nodes.Statements.Conditional.If

def p_if_01(p):
    'conditional_statement : IF LEFT_PAREN expression RIGHT_PAREN compound_statement ELSE compound_statement'
    p[0] = Nodes.Statements.Conditional.If.Node(p[3],p[5],p[7])

def p_if_02(p):
    'conditional_statement : IF LEFT_PAREN expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Conditional.If.Node(p[3],p[5])

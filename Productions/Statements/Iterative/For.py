import Nodes.Statements.Iterative.For
import Nodes.Statements.Iterative.LegacyFor

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

def p_for_05(p):
    'iterative_statement : FOR LEFT_PAREN variable_declaration expression SEMICOLON assignment_statement RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.LegacyFor.Node(p[3],p[4],p[6],p[8])

def p_for_06(p):
    'iterative_statement : FOR LEFT_PAREN variable_declaration expression SEMICOLON expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.LegacyFor.Node(p[3],p[4],p[6],p[8])

def p_for_07(p):
    'iterative_statement : FOR LEFT_PAREN expression SEMICOLON expression SEMICOLON assignment_statement RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.LegacyFor.Node(p[3],p[5],p[7],p[9])

def p_for_08(p):
    'iterative_statement : FOR LEFT_PAREN expression SEMICOLON expression SEMICOLON expression RIGHT_PAREN compound_statement'
    p[0] = Nodes.Statements.Iterative.LegacyFor.Node(p[3],p[5],p[7],p[9])

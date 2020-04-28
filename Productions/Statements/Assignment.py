import Nodes.Statements.Assignment
import Nodes.Statements.StructAssignment

def p_rule_01(p):
    'assignment_statement : PUT expression IN IDENTIFIER SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[4],'=',p[2])

def p_rule_02(p):
    'assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.Assignment.Node(p[1],p[2],p[3])

def p_rule_03(p):
    'assignment_statement : IDENTIFIER DOT IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = Nodes.Statements.StructAssignment.Node(p[1],p[3],p[5])

import Nodes.Statements.Declaration.List
import Nodes.NoOperation

def p_declaration_list_01(p):
    'declaration_list : statement declaration_list'
    p[0] = Nodes.Statements.Declaration.List.Node(p[1],p[2])

def p_declaration_list_02(p):
    'declaration_list : function_declaration declaration_list'
    p[0] = Nodes.Statements.Declaration.List.Node(p[1],p[2])

def p_declaration_list_03(p):
    'declaration_list : struct_declaration declaration_list'
    p[0] = Nodes.Statements.Declaration.List.Node(p[1],p[2])

def p_declaration_list_04(p):
    'declaration_list : empty'
    p[0] = p[1]

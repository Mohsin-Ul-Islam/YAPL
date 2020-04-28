import Nodes.Statements.Declaration.Struct

def p_struct_01(p):
    'struct_declaration : STRUCT IDENTIFIER LEFT_BRACE variable_declaration_list RIGHT_BRACE'
    p[0] = Nodes.Statements.Declaration.Struct.Node(p[2],p[4])

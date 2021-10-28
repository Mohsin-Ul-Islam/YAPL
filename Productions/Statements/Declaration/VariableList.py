import Nodes.Statements.Declaration.VariableList


def p_var_declaration_list_01(p):
    "variable_declaration_list : variable_declaration variable_declaration_list"
    p[0] = Nodes.Statements.Declaration.VariableList.Node(p[1], p[2])


def p_var_declaration_list_02(p):
    "variable_declaration_list : empty"
    p[0] = p[1]

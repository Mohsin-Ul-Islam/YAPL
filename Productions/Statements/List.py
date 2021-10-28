import Nodes.Statements.List


def p_statement_list(p):
    """
    statement_list : statement statement_list
    """
    p[0] = Nodes.Statements.List.Node(p[1], p[2])


def p_statement_list_empty(p):
    "statement_list : empty"
    pass

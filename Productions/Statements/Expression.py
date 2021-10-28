import Nodes.Statements.Expression


def p_statement_expression(p):
    """expression_statement : expression SEMICOLON
    expression_statement : SEMICOLON
    """
    try:
        p[0] = Nodes.Statements.Expression.Node(p[1])
    except:
        pass

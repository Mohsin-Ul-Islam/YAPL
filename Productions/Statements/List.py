import Nodes.Statements.List

def p_statement_list(p):
    '''
        statement_list : statement statement_list
                       |
    '''

    try:
        p[0] = Nodes.Statements.List.Node(p[1],p[2])
    except:
        pass

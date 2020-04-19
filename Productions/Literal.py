import Nodes.Identifier
import Nodes.Literal

###########################################################
######### Literals ########################################
###########################################################

def p_literal_identifier(p):
    'literal : IDENTIFIER'
    p[0] = Nodes.Identifier.Node(p[1])


def p_literal(p):
    '''

    literal : DOUBLE
            | INTEGER
            | STRING

    '''
    p[0] = Nodes.Literal.Node(p[1])

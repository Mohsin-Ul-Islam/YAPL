import Nodes.Identifier
import Nodes.Literal
import Nodes.StructMember

###########################################################
######### Literals ########################################
###########################################################

def p_literal_struct(p):
    'literal : IDENTIFIER DOT IDENTIFIER'
    p[0] = Nodes.StructMember.Node(p[1],p[3])

def p_literal_identifier(p):
    'literal : IDENTIFIER'
    p[0] = Nodes.Identifier.Node(p[1])

def p_literal(p):
    '''

    literal : DOUBLE
            | INTEGER
            | STRING
            | TRUE
            | FALSE

    '''
    p[0] = Nodes.Literal.Node(p[1])

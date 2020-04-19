import Nodes.Factor

###########################################################
######### Factors #########################################
###########################################################
def p_factor(p):
    'factor : literal'
    p[0] = Nodes.Factor.Node(p[1])

def p_factor_expression(p):
    'factor : LEFT_PAREN expression RIGHT_PAREN'
    p[0] = Nodes.Factor.Node(p[2])

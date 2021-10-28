import Nodes.Term

###########################################################
######### Terms ###########################################
###########################################################
def p_term_factor_product(p):
    "term : term PRODUCT factor"
    p[0] = Nodes.Term.Node(p[1], "*", p[3])


def p_term_factor_divide(p):
    "term : term DIVIDE factor"
    p[0] = Nodes.Term.Node(p[1], "/", p[3])


def p_term_factor(p):
    "term : factor"
    p[0] = Nodes.Term.Node(p[1])

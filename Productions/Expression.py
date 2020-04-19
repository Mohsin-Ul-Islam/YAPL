import Nodes.Expression

###########################################################
######### Expressions #####################################
###########################################################
def p_expression_negative(p):
    'expression : MINUS term'
    p[0] = Nodes.Expression.Node(p[2],'-')

def p_expression_not(p):
    'expression : NOT term'
    p[0] = Nodes.Expression.Node(p[2],'!')

def p_expression_gte(p):
    'expression : expression GTE term'
    p[0] = Nodes.Expression.Node(p[1],'>=',p[3])

def p_expression_lte(p):
    'expression : expression LTE term'
    p[0] = Nodes.Expression.Node(p[1],'<=',p[3])

def p_expression_gt_descriptive(p):
    'expression : expression IS GREATER THAN term'
    p[0] = Nodes.Expression.Node(p[1],'>',p[5])

def p_expression_lt_descriptive(p):
    'expression : expression IS LESS THAN term'
    p[0] = Nodes.Expression.Node(p[1],'<',p[5])

def p_expression_gt(p):
    'expression : expression GT term'
    p[0] = Nodes.Expression.Node(p[1],'>',p[3])

def p_expression_lt(p):
    'expression : expression LT term'
    p[0] = Nodes.Expression.Node(p[1],'<',p[3])

def p_expression_equal_is(p):
    'expression : expression IS term'
    p[0] = Nodes.Expression.Node(p[1],'==',p[3])

def p_expression_equal(p):
    'expression : expression EQUALS term'
    p[0] = Nodes.Expression.Node(p[1],'==',p[3])

def p_expression_or(p):
    'expression : expression OR term'
    p[0] = Nodes.Expression.Node(p[1],'||',p[3])

def p_expression_and(p):
    'expression : expression AND term'
    p[0] = Nodes.Expression.Node(p[1],'&&',p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = Nodes.Expression.Node(p[1],'+',p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = Nodes.Expression.Node(p[1],'-',p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = Nodes.Expression.Node(p[1])

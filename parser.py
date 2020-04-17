# importing yacc module from ply
import ply.yacc as yacc
from lexer import tokens
from nodes import *

# precedence rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'PRODUCT', 'DIVIDE'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT')
)

# specifying grammar rules as single well defined functions
def p_program(p):
    'program : statement_list'
    p[0] = ProgramNode(p[1])

def p_statement(p):
    '''
        statement : assignment_statement
                  | expression_statement
                  | iterative_statement
                  | conditional_statement
                  | compound_statement
                  | print_statement
    '''
    p[0] = StmntNode(p[1])


def p_statement_list(p):
    '''
        statement_list : statement statement_list
                       |
    '''

    try:
        p[0] = StmntListNode(p[1],p[2])
    except:
        pass

def p_conditional_statement_if_else(p):
    'conditional_statement : IF LEFT_PAREN expression RIGHT_PAREN compound_statement ELSE compound_statement'
    p[0] = ConditionalStmntNode(p[3],p[5],p[7])

def p_conditional_statement_if(p):
    'conditional_statement : IF LEFT_PAREN expression RIGHT_PAREN compound_statement'
    p[0] = ConditionalStmntNode(p[3],p[5])

def p_iterative_statement_while(p):
    'iterative_statement : WHILE LEFT_PAREN expression RIGHT_PAREN compound_statement'
    p[0] = IterativeStmntNode(p[3],p[5])

def p_compound_statement(p):
    'compound_statement : LEFT_BRACE statement_list RIGHT_BRACE'
    p[0] = CompoundStmntNode(p[2])

def p_statement_expression(p):
    '''expression_statement : expression SEMICOLON
       expression_statement : SEMICOLON
    '''
    try:
        p[0] = ExpressionStmntNode(p[1])
    except:
        pass

###########################################################
######### Print Statements ################################
###########################################################
def p_statement_log(p):
    'print_statement : LOG LEFT_PAREN expression RIGHT_PAREN SEMICOLON'
    p[0] = PrintStmntNode(p[3])



###########################################################
######### Assignment Statements  ##########################
###########################################################
def p_statement_descriptive(p):
    'assignment_statement : PUT expression IN IDENTIFIER SEMICOLON'
    p[0] = AssignmentStmntNode(p[4],p[2])

def p_statement_assignment(p):
    'assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = AssignmentStmntNode(p[1],p[3])

def p_statement_assignment_let(p):
    'assignment_statement : LET IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = AssignmentStmntNode(p[2],p[4])


###########################################################
######### Expressions #####################################
###########################################################
def p_expression_negative(p):
    'expression : MINUS term'
    p[0] = ExpressionNode(p[2],'-')

def p_expression_not(p):
    'expression : NOT term'
    p[0] = ExpressionNode(p[2],'!')

def p_expression_equal(p):
    'expression : expression EQUALS term'
    p[0] = ExpressionNode(p[1],'==',p[3])

def p_expression_or(p):
    'expression : expression OR term'
    p[0] = ExpressionNode(p[1],'||',p[3])

def p_expression_and(p):
    'expression : expression AND term'
    p[0] = ExpressionNode(p[1],'&&',p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ExpressionNode(p[1],'+',p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ExpressionNode(p[1],'-',p[3])


def p_expression_term(p):
    'expression : term'
    p[0] = ExpressionNode(p[1])



###########################################################
######### Terms ###########################################
###########################################################
def p_term_factor_product(p):
    'term : term PRODUCT factor'
    p[0] = TermNode(p[1], '*', p[3])

def p_term_factor_divide(p):
    'term : term DIVIDE factor'
    p[0] = TermNode(p[1],'/',p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = TermNode(p[1])


###########################################################
######### Factors #########################################
###########################################################
def p_factor(p):
    'factor : literal'
    p[0] = FactorNode(p[1])

def p_factor_expression(p):
    'factor : LEFT_PAREN expression RIGHT_PAREN'
    p[0] = FactorNode(p[2])


###########################################################
######### Literals ########################################
###########################################################
def p_literal_identifier(p):
    'literal : IDENTIFIER'
    p[0] = IdentifierNode(p[1])

def p_literal(p):
    '''

    literal : DOUBLE
            | INTEGER
            | STRING

    '''
    p[0] = LiteralNode(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!",p)
    exit()

parser = yacc.yacc()

def printTree(tree,parent='',indent = ''):

    print(parent,tree)
    for child in tree.children:
        indent += "\t"
        printTree(child,tree.type)


def main():


    file = open('hello_world.yapl','r')
    code = file.read()
    tree = parser.parse(code)
    print(tree.visit())

    '''
    while True:

        code = input('yapl >> ')
        if(code == 'quit' or code == 'exit'):
            break
        tree = parser.parse(code)
        print(tree.visit())
    '''

if __name__ == '__main__':

    main()

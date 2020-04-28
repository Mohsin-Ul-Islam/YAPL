import Nodes.Statements.Generic

def p_statement(p):
    '''
        statement : assignment_statement
                  | expression_statement
                  | iterative_statement
                  | conditional_statement
                  | compound_statement
                  | print_statement
                  | function_call
                  | variable_declaration
    '''
    p[0] = Nodes.Statements.Generic.Node(p[1])

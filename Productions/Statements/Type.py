def p_type_specifier(p):
    '''
        type_specifier : TYPE_BOOL
                       | TYPE_INT
                       | TYPE_CHAR
                       | TYPE_DOUBLE
                       | TYPE_STRING
    '''
    p[0] = p[1]

# importing the required lex module of ply library
import ply.lex as lex

# defining tokens for the lexer
tokens = [

    'LEFT_BRACE',    # token for left brace '{'
    'RIGHT_BRACE',   # token for right brace '}'

    'LEFT_PAREN',   # token for left paranthesis '('
    'RIGHT_PAREN',  # token for right paranthesis ')'

    'PRODUCT',      # token for product operator '*'
    'DIVIDE',       # token for division operator '/'
    'MODULUS',      # token for remainder operator '%'

    'PLUS',         # token for addition operator '+'
    'MINUS',        # token for difference operator '-'

    'DOUBLE',       # token for floating point numbers
    'INTEGER',      # token for integer numbers [0-9] +ve and -ve

    'STRING',        # token for strings
    'IDENTIFIER',    # token for variable names

    'SEMICOLON',      # token for statement endings
    'ASSIGN',        # token for assignment operator
    'COMMA'

]

keywords = {

    'if'        : 'IF',        # keyword for if statements
    'else'      : 'ELSE',      # keyword for else
    'and'       : 'AND',       # logical AND
    'or'        : 'OR',        # logical OR
    'not'       : 'NOT',       # logical NOT
    'is'        : 'EQUALS',    # equality
    'equals'    : 'EQUALS',    # equality
    'return'    : 'RETURN',     # returning values
    'in'        : 'IN',
    'put'       : 'PUT',
    'for'       : 'FOR',
    'while'     : 'WHILE',
    'do'        : 'DO',
    'structure' : 'STRUCT',
    'object'    : 'OBJECT',
    'break'     : 'BREAK',
    'skip'      : 'SKIP',
    'log'       : 'LOG',
    'subroutine' : 'FUNCTION',
    'let'       : 'LET'
}

tokens += list(keywords.values())


###########################################################
######### defining regular expressions for tokens #########
###########################################################

def t_COMMA(token):
    r','
    return token

# token specification for semi colon
def t_SEMICOLON(token):
    r';'
    return token

# token specification for logical AND '&&'
def t_AND(token):
    r'&&'
    return token

# token specification for logical OR '||'
def t_OR(token):
    r'\|\|'
    return token

# token specification for unary logical NOT '!'
def t_NOT(token):
    r'!'
    return token

# token specification for equality '=='
def t_EQUALS(token):
    r'=='
    return token

# token specification for assignment operator '='
def t_ASSIGN(token):
    r'='
    return token


# token specification for left brace '{'
def t_LEFT_BRACE(token):
    r'\{'
    return token

# token specification for right brace '}'
def t_RIGHT_BRACE(token):
    r'\}'
    return token

# token specification for left paranthesis '('
def t_LEFT_PAREN(token):
    r'\('
    return token

# token specification for right paranthesis ')'
def t_RIGHT_PAREN(token):
    r'\)'
    return token

# token specification for product operator '*'
def t_PRODUCT(token):
    r'\*'
    return token

# token specification for division operator '/'
def t_DIVIDE(token):
    r'/'
    return token

# token specification for modulus (remainder) operator '%'
def t_MODULUS(token):
    r'%'
    return token

# token specification for addition operator '+'
def t_PLUS(token):
    r'\+'
    return token

# token specification for difference operator '-'
def t_MINUS(token):
    r'-'
    return token

# token specification for floating point numbers
def t_DOUBLE(token):
    r'[0-9]+\.[0-9]+'
    token.value = float(token.value)
    return token

# token specification for integer numbers [0-9]
def t_INTEGER(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

# token specification for strings
def t_STRING(token):
    r'".*"'
    token.value = str(token.value)
    token.value = token.value[1:-1]
    return token

# token specification for variable names and keywords
def t_IDENTIFIER(token):
    r'[_A-Za-z][_A-Za-z]*'
    token.type = keywords.get(token.value,'IDENTIFIER')
    return token

# token specification for newline characters
def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

# token for ignoring white space
t_ignore = ' \t'

# token for error checking during lexing
def t_error(token):
    print("\nInvalid token encountered: '" + str(token.value[0]) + "' | at:[" + str(token.lexer.lineno) + "," + str(token.lexer.lexpos) + "]")
    token.lexer.skip(1)


###########################################################
######### End of token specializations ####################
###########################################################

lexer = lex.lex()

def main():

    while True:

        code = input('yapl >> ')
        if(code == 'quit' or code == 'exit'):
            break
        lexer.input(code)
        for token in lexer:
            print(token)


if __name__ == '__main__':
    main()

# importing yacc module from ply
import ply.yacc as yacc
from lexer import tokens


# precedence rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'PRODUCT', 'DIVIDE'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT')
)


'''
from Productions.Statements.Declaration         import *
from Productions.Statements.Type                import *
'''

from Productions.Program                        import *
from Productions.Statements.Generic             import *
from Productions.Statements.List                import *
from Productions.Functions.Call                 import *
from Productions.Functions.Generic              import *
from Productions.Statements.Conditional.If      import *
from Productions.Statements.Iterative.For       import *
from Productions.Statements.Iterative.DoWhile   import *
from Productions.Statements.Iterative.While     import *
from Productions.Statements.Compound            import *
from Productions.Statements.Expression          import *
from Productions.Statements.Print               import *
from Productions.Functions.Arguments            import *
from Productions.Statements.Assignment          import *
from Productions.Expression                     import *
from Productions.Term                           import *
from Productions.Factor                         import *
from Productions.Literal                        import *
from Productions.Error                          import *




parser = yacc.yacc(start='program')

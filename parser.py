# importing yacc module from ply
import ply.yacc as yacc
from lexer import tokens


# precedence rules

precedence = (
    ('left','COMMA'),
    ('right','ASSIGN'),
    ('left','OR'),
    ('left','AND'),
    ('left','EQUALS'),
    ('left','LT','LTE','GT','GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'EXP'),
    ('left', 'PRODUCT', 'DIVIDE'),
    ('right', 'NOT'),
    ('right','INCREMENT','DECREMENT')
)


# importing grammar rules -- productions

from Productions.Program                                import *
from Productions.Statements.Declaration.Struct          import *
from Productions.Statements.Declaration.Variable        import *
from Productions.Statements.Declaration.Function        import *
from Productions.Statements.Declaration.List            import *
from Productions.Statements.Declaration.VariableList    import *
from Productions.Statements.Type                        import *
from Productions.Statements.Generic                     import *
from Productions.Statements.List                        import *
from Productions.Functions.Call                         import *
from Productions.Statements.Conditional.If              import *
from Productions.Statements.Iterative.For               import *
from Productions.Statements.Iterative.DoWhile           import *
from Productions.Statements.Iterative.While             import *
from Productions.Statements.Compound                    import *
from Productions.Statements.Expression                  import *
from Productions.Statements.Print                       import *
from Productions.Functions.Arguments                    import *
from Productions.Statements.Assignment                  import *
from Productions.Expression                             import *
from Productions.Term                                   import *
from Productions.Factor                                 import *
from Productions.Literal                                import *
from Productions.Error                                  import *
from Productions.Empty                                  import *



parser = yacc.yacc(start='program')

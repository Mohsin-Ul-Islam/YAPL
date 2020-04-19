import Nodes.Program
import Nodes.NoOperation

# specifying grammar rules as single well defined functions
def p_program(p):
    'program : statement_list'
    if not p[1]:
        p[0] = Nodes.NoOperation.Node()
    else:
        p[0] = Nodes.Program.Node(p[1])

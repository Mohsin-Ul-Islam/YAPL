import Nodes.Program
import Nodes.NoOperation

# specifying grammar rules as single well defined functions
def p_program_01(p):
    'program : declaration_list'
    p[0] = Nodes.Program.Node(p[1])

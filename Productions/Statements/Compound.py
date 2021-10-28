import Nodes.Statements.Compound
import Nodes.NoOperation


def p_compound_statement(p):
    "compound_statement : LEFT_BRACE statement_list RIGHT_BRACE"
    p[0] = Nodes.Statements.Compound.Node(p[2])

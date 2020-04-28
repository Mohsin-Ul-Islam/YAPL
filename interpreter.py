import sys
from parser import parser
from Errors import *

def execute_program(filename):
    try:
        file = open('./test_cases/' + filename,'r')
        code = file.read()
        tree = parser.parse(code)
        tree.visit()
    except (VariableTypeError,VariableNotDefinedError,RedeclarationError,DivisionByZeroError) as error:
        print(error)
        exit(1)

def run_interpreter():
        while True:

            code = input('yapl >>> ')
            if(code == 'quit' or code == 'exit'):
                break
            try:
                tree = parser.parse(code)
                print(tree.visit())
            except VariableTypeError as error:
                print(error)
            except VariableNotDefinedError as error:
                print(error)
            except RedeclarationError as error:
                print(error)
            except DivisionByZeroError as error:
                print(error)
            except KeyboardInterrupt:
                print("Quitting...")
                exit(1)
            except Exception:
                print()
def main():

    if len(sys.argv) > 1:
        execute_program(sys.argv[1])
    else:
        run_interpreter()

if __name__ == '__main__':

    main()

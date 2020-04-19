import sys
from parser import parser

def execute_program(filename):
    file = open('hello_world.yapl','r')
    code = file.read()
    tree = parser.parse(code)
    print(tree.visit())

def run_interpreter():
        while True:

            code = input('yapl >>> ')
            if(code == 'quit' or code == 'exit'):
                break
            tree = parser.parse(code)
            print(tree.visit())

def main():

    if len(sys.argv) > 1:
        execute_program(sys.argv[1])
    else:
        run_interpreter()

if __name__ == '__main__':

    main()

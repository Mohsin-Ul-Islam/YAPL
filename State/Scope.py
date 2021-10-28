class Scope:
    def __init__(self):

        self.level = 0

    def push(self):
        self.level += 1

    def pop(self):
        self.level -= 1

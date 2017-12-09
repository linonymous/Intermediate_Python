import sys
sys.path.append("C:\Users\Swapnil.Walke\Intermediate_Python\Tic-Tac-Toe")
from person import Person

class Player(Person):

    def __init__(self, name):
        Person.__init__(self, name)
        self.moves = []
        self.status = "STARTED"

    def make_move(self, index):
        self.moves.append(index)
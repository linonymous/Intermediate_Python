import sys
from controller import Controller
from player import Player
sys.path.append("C:\Users\Swapnil.Walke\Intermediate_Python\Tic-Tac-Toe")


class TicTacToeController(Controller):

    log_file = "tic_tac_toe.log"

    def __init__(self):
        Controller.__init__(self, self.log_file)
        self.logging.info("TicTacToe controller initiated")
        self.matrix = []
        self.board = []
        for i in range(1, 9):
            self.board[i] = '_'

        for i in range(1,9,3):
            self.matrix.append(range(i, i+3))
        self.logging.info("matrix has been built")
        self.logging.info(str(self.matrix))

    def _pre_play(self):
        print "Welcome to tic tac toe"
        print "Enter number of players"
        a = int(raw_input())
        if a == 1:
            self.logging.info("One player game has been started....")
            print "Welcome to the game"
            print "Enter the name of player one:"
            player_one = raw_input()
            self.player_one = Player(player_one)
            print "Welcome " + player_one + "!! you will play against JARVIS!"
            self.player_two = Player("--JARVIS--")
            self.logging.info(str(self.player_one) + " is playing against " + str(self.player_two))
            self._play_bot()
        if a == 2:
            self.logging.debug("Two player game has been started....")
            print "Welcome to the game"
            print "Enter the name of player one:"
            """Enter the names of the player, and initiate the players"""
            player_one = raw_input()
            print "Enter the name of player two:"
            player_two = raw_input()
            self.logging.debug("player " + player_one + " and " + " player " + player_two + " has started playing...")
            self.player_one = Player(player_one)
            self.player_two = Player(player_two)
            self._play()

    def display_matrix(self):
        """display the matrix"""
        self.logging.debug(str(self.matrix))
        for i in self.matrix:
            stri = ""
            for j in i:
                stri += str(j) + " "
            print stri

    @staticmethod
    def print_space():
        """display 3 spaces"""
        for i in range(3):
            print ""

    def win(self, player):
        """check the winning condition or check the draw condition"""
        if player == 1:
            a = self.player_one.moves
        else:
            a = self.player_two.moves
        winning_moves = []
        for i in range(1, 9, 3):
            winning_moves.append(range(i, i+3))
        for i in range(1, 4):
            winning_moves.append(range(i, i+7, 3))
        winning_moves.append([1, 5, 9])
        winning_moves.append([3, 5, 7])
        for move in winning_moves:
            flg = True
            for index in move:
                if index not in a:
                    flg = False
                    break
            if flg:
                return True, player
        if len(self.player_one.moves) + len(self.player_two.moves) == 9:
            print " Games is drawn"
            self.logging.debug("Game is draw, nobody won")
            self.logging.debug("Enjoy the game again :)")
            sys.exit(100)
        return False, player

    def is_valid_move(self, m):
        if m < 1 or m > 9:
            print "Wrong input"
            return -1
        if m in self.player_one.moves or m in self.player_two.moves:
            return -2

    def min_max(self, depth, isMax):

        #Check which player has won and return score accordingly
        ret, player = self.win(1)
        if ret == True:
            print"Congratulations, player 1 has won!!"
            return -10

        #If no moves left, return score to be 0
        if ret == False:
            return 0

        #This is Our player bot, and it is maximizer
        ret, player = self.win(2)
        if ret == True:
            print"Congratulations, player 2 has won!!"
            return 10

        #If this is Maximizer move
        if(isMax):
            best = -1000

            #Traverse all the cells
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if self.board[i][j] == '_':

                        #make the move
                        self.board[i][j] = 'X'

                        #Call min_max recursively and find out the maximun value
                        best = max(best, self.min_max(depth + 1, not(isMax)))
            return best
        else:
            best = 1000

            # Traverse all the cells
            for i in range(0, 3, 1):
                for j in range(0, 3, 1):
                    if self.board[i][j] == '_':
                        # make the move
                        self.board[i][j] = 'O'

                        # Call min_max recursively and find out the minimum value
                        best = min(best, self.min_max(depth + 1, not (isMax)))
            return best

    def find_best_move(self):
        best_val = -1000
        best_row = -1
        best_col = -1

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '_':

                    #Make the move
                    self.board[i][j] = 'X'
                    move_val = self.min_max(0, False)

                    #Undo the move
                    self.board[i][j] = '_'

                    #if value of current move > best_value, update
                    if move_val > best_val:
                        best_val = move_val
                        best_row = i
                        best_col = j

        return best_row, best_col


    def _play_bot(self):
        print "Lets start the game..."
        players = [self.player_one.name, self.player_two.name]
        flg = 1
        while True:
            self.print_space()
            self.display_matrix()
            self.print_space()
            if players[flg-1] == "--JARVIS--":
                m = self.find_best_move()
            else:
                print "Enter move for player " + str(players[flg-1])
                m = int(raw_input())
            ret = self.is_valid_move(m)
            if ret == -1:
                continue
            elif ret == -2:
                print "Invalid Move, already played.."
                continue
            if flg == 1:
                self.player_one.make_move(m)
                flg = 2
            else:
                self.player_two.make_move(m)
                flg = 1
            if flg == 2:
                ch = "X"
            else:
                ch = "O"
            m -= 1
            for i in self.matrix:
                if (m + 1) in i:
                    m = m % 3
                    i.pop(m)
                    i.insert(m, ch)
            ret, player = self.win(1 if flg == 2 else 2)
            if ret is True:
                print " Congratulations! Player " + str(player) + " have won the match!"
                break

    def _play(self):
        print"Lets start the game"
        flg = 1
        while True:
            self.print_space()
            self.display_matrix()
            self.print_space()
            print"Enter move for player " + str(flg)
            m = int(raw_input())

            ret = self.is_valid_move(m)
            if ret == -1:
                continue
            elif ret == -2:
                print "Invalid Move, already played.."
                continue
            if flg == 1:
                self.player_one.make_move(m)
                flg = 2
            else:
                self.player_two.make_move(m)
                flg = 1
            if flg == 2:
                ch = "X"
            else:
                ch = "O"
            m -= 1
            for i in self.matrix:
                if (m+1) in i:
                    m = m % 3
                    i.pop(m)
                    i.insert(m, ch)
            ret, player = self.win(1 if flg == 2 else 2)
            if ret is True:
                print " Congratulations! Player " + str(player) + " have won the match!"
                break

    def initiate(self):
        self._pre_play()


game = TicTacToeController()
game.initiate()
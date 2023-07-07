import random
import engine
import board

class Game():
    e = engine.Engine()
    b = board.Board()

    def player_input(self):

        player1 = input("Please pick a marker 'X' or 'O'")
        while player1 != 'X' and player1 != 'O':
            print("Wrong character")
            player1 = input("Please pick a marker 'X' or 'O'")

        return player1

    def choose_first(self):
        players = ['Player 1', 'Player 2']
        i = random.randint(0, 1)
        return players[i]

    def player_choice(self, board):
        right = False
        while not right:
            position = int(input('Please enter a number from 1 to 9 that is not filled'))

            while position not in range(1, 10):
                print("Wrong choice")
                position = int(input('Please enter a number from 1 to 9'))

            right = self.b.space_check(board, position)

        return position

    def game_loop(self):
        print('Welcome to Tic Tac Toe!')

        while True:
            # Set the game up here
            self.b.game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

            print('Player 1')
            m1 = self.player_input()

            if m1 == 'X':
                m2 = 'O'
            else:
                m2 = 'X'

            play = {'Player 1': m1, 'Player 2': m2}

            first = self.choose_first()
            if first == 'Player 1':
                second = 'Player 2'
            else:
                second = 'Player 1'
            print('First goes: ' + first)

            self.b.display_board(self.b.game_board)
            while True:
                print(first + ' turn')
                num = self.player_choice(self.b.game_board)
                self.b.place_marker(self.b.game_board, play[first], num)
                self.b.display_board(self.b.game_board)
                if self.e.win_check(self.b.game_board, play[first]):
                    print(first + ' won')
                    break
                if self.b.full_board_check(self.b.game_board):
                    print('No one won')
                    break
                # -------------------------------------------------
                print(second + ' turn')
                num = self.player_choice(self.b.game_board)
                self.b.place_marker(self.b.game_board, play[second], num)
                self.b.display_board(self.b.game_board)
                if self.e.win_check(self.b.game_board, play[second]):
                    print(second + ' won')
                    break
                if self.b.full_board_check(self.b.game_board):
                    print('No one won')
                    break

            if not self.e.replay():
                break

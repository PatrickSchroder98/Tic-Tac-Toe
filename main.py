import random

test_board = ['#','X','O','X','O','X','O','X','O','X']
start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board(board):

   print(board[1] + "|" + board[2] + "|" + board[3] + "\n" +
         board[4] + "|" + board[5] + "|" + board[6] + "\n" +
         board[7] + "|" + board[8] + "|" + board[9])


def player_input():

   player1 = input("Please pick a marker 'X' or 'O'")
   while player1 != 'X' and player1 != 'O':
      print("Wrong character")
      player1 = input("Please pick a marker 'X' or 'O'")

   return player1


def place_marker(board, marker, position):

   board[position] = marker


def win_check(board, mark):
   if board[1]==mark and board[2]==mark and board[3]==mark:
      return True
   if board[4]==mark and board[5]==mark and board[6]==mark:
      return True
   if board[7]==mark and board[8]==mark and board[9]==mark:
      return True

   if board[1] == mark and board[4] == mark and board[7] == mark:
      return True
   if board[2] == mark and board[5] == mark and board[8] == mark:
      return True
   if board[3] == mark and board[6] == mark and board[9] == mark:
      return True

   if board[1] == mark and board[5] == mark and board[9] == mark:
      return True
   if board[3] == mark and board[5] == mark and board[7] == mark:
      return True

   return False


def choose_first():
   players = ['Player 1', 'Player 2']
   i = random.randint(0, 1)
   return players[i]


def space_check(board, position):
   if board[position] == 'X' or board[position] == 'O':
      return False
   return True


def full_board_check(board):
   for i in range(1,10):
      if board[i] != 'X' and board[i] != 'O':
         return False
   return True


def player_choice(board):
   right = False
   while not right:
      position = int(input('Please enter a number from 1 to 9 that is not filled'))

      while position not in range (1,10):
         print("Wrong choice")
         position = int(input('Please enter a number from 1 to 9'))

      right = space_check(board, position)

   return position


def replay():
   inp = input("Do you want to play again?('Y' or 'N')")
   while inp != 'Y' and inp != 'N':
      print("Wrong character")
      inp = input("Do you want to play again?('Y' or 'N')")

   if inp == 'Y':
      return True
   return False


print('Welcome to Tic Tac Toe!')

while True:
   # Set the game up here
   game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

   print('Player 1')
   m1 = player_input()

   if m1 == 'X':
      m2 = 'O'
   else:
      m2 = 'X'

   play = {'Player 1': m1, 'Player 2': m2}

   first = choose_first()
   if first == 'Player 1':
      second = 'Player 2'
   else:
      second = 'Player 1'
   print('First goes: ' + first)

   display_board(game_board)
   while True:
      print(first + ' turn')
      num = player_choice(game_board)
      place_marker(game_board, play[first], num)
      display_board(game_board)
      if win_check(game_board, play[first]):
         print(first + ' won')
         break
      if full_board_check(game_board):
         print('No one won')
         break
      #-------------------------------------------------
      print(second + ' turn')
      num = player_choice(game_board)
      place_marker(game_board, play[second], num)
      display_board(game_board)
      if win_check(game_board, play[second]):
         print(second + ' won')
         break
      if full_board_check(game_board):
         print('No one won')
         break


   if not replay():
      break



#tests
#display_board(test_board)
#marker = player_input()
#place_marker(test_board,'$',8)
#display_board(test_board)
#print(win_check(test_board,'X'))
#print(choose_first())
#print(space_check(test_board, 1))
#print(full_board_check(test_board))
#player_choice(test_board)
#print(replay())
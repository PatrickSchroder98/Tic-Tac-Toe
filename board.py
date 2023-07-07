class Board():
    game_board =  ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display_board(self, board):
        print(board[1] + "|" + board[2] + "|" + board[3] + "\n" +
              board[4] + "|" + board[5] + "|" + board[6] + "\n" +
              board[7] + "|" + board[8] + "|" + board[9])

    def place_marker(self, board, marker, position):
        board[position] = marker

    def space_check(self, board, position):
        if board[position] == 'X' or board[position] == 'O':
            return False
        return True

    def full_board_check(self, board):
        for i in range(1, 10):
            if board[i] != 'X' and board[i] != 'O':
                return False
        return True

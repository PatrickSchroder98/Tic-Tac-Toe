class Engine():

    def win_check(self, board, mark):
        if board[1] == mark and board[2] == mark and board[3] == mark:
            return True
        if board[4] == mark and board[5] == mark and board[6] == mark:
            return True
        if board[7] == mark and board[8] == mark and board[9] == mark:
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

    def replay(self):
        inp = input("Do you want to play again?('Y' or 'N')")
        while inp != 'Y' and inp != 'N':
            print("Wrong character")
            inp = input("Do you want to play again?('Y' or 'N')")

        if inp == 'Y':
            return True
        return False
def play_turn(game_board, col, row, val):
    if col not in range (0,3) or row not in range(0,3) or game_board[row][col] == "X" or game_board[row][col] == "O":
        return False
    game_board[row][col] = val
    return True
if __name__ == "__main__":
    game_board = [['', 'X', 'X'], ['', '', ''], ['O', 'X', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
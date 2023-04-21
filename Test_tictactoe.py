"""
NAME: <WEI ZHAO>
SEMESTER: <Spring 2023>
"""

from tictactoe_minimax import print_board, check_win, get_ai_move, minimax, board

def test_check_win():
    # Test for no win
    board[0] = ['X', 'O', 'X']
    board[1] = ['O', 'O', 'X']
    board[2] = ['X', 'X', 'O']
    assert not check_win('X')
    assert not check_win('O')

    # Test for row win
    board[0] = ['X', 'X', 'X']
    board[1] = ['O', 'O', ' ']
    board[2] = [' ', ' ', ' ']
    assert check_win('X')
    assert not check_win('O')

    # Test for column win
    board[0] = ['X', 'O', ' ']
    board[1] = ['X', 'O', ' ']
    board[2] = ['X', ' ', ' ']
    assert check_win('X')
    assert not check_win('O')

    # Test for diagonal win
    board[0] = ['X', 'O', ' ']
    board[1] = ['O', 'X', ' ']
    board[2] = [' ', ' ', 'X']
    assert check_win('X')
    assert not check_win('O')

def test_get_ai_move():
    # Test for an obvious winning move
    board[0] = ['O', 'O', ' ']
    board[1] = ['X', 'X', ' ']
    board[2] = ['X', ' ', ' ']
    assert get_ai_move() == (0, 2)

    # Test for an obvious blocking move
    board[0] = ['X', 'X', ' ']
    board[1] = ['O', 'O', ' ']
    board[2] = [' ', ' ', ' ']
    assert get_ai_move() == (0, 2)

def test_minimax():
    # Test for a winning move
    board[0] = ['O', 'O', ' ']
    board[1] = ['X', 'X', ' ']
    board[2] = ['X', ' ', ' ']
    assert minimax(board, 0, True) == 1

    # Test for a losing move
    board[0] = ['X', 'X', ' ']
    board[1] = ['O', 'O', ' ']
    board[2] = [' ', ' ', ' ']
    assert minimax(board, 0, False) == -1

    # Test for a draw
    board[0] = ['X', 'O', 'X']
    board[1] = ['O', 'O', 'X']
    board[2] = ['X', 'X', 'O']
    assert minimax(board, 0, True) == 0
    assert minimax(board, 0, False) == 0

def run_tests():
    test_check_win()
    test_get_ai_move()
    test_minimax()

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()

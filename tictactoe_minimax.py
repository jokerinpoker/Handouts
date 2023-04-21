"""
NAME: <WEI ZHAO>
SEMESTER: <Spring 2023>
"""

#Define a function to print out the current state of the board
def print_board():
    """Prints out the current state of the board"""
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

#Define the initial board as a 3x3 grid of empty cells
board = [[' ' for _ in range(3)] for _ in range(3)]

def check_win(player):
    """Check rows"""
    for row in board:
        if all(cell == player for cell in row):
            return True
    """Check columns"""
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    """Check diagonals"""
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

#Define a function to determine the best move for the AI by minimax algorithm
def get_ai_move():
    """Minimax algorithm to determine the best move for the AI"""
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


#Define the minimax algorithm to recursively search all possible outcomes
def minimax(board, depth, is_maximizing):
    if check_win('O'):
        return 1
    elif check_win('X'):
        return -1
    elif ' ' not in [cell for row in board for cell in row]:
        return 0
    
    if is_maximizing:
        #If it's AI's turn, maximize the score
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    #make a move
                    board[i][j] = 'O'
                    #Evalute the score of this move
                    score = minimax(board, depth+1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    
    else:
        """If it's the player's turn, minimize the score"""
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    #make a move
                    board[i][j] = 'X'
                    #Evalute the score of this move
                    score = minimax(board, depth+1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


#Define the main game loop
def play_game():
    """Print out the initial state of the board"""
    print_board()
    while True:
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        #If the cell is already occupied, prompt the player to enter another move
        if board[row][col] == ' ':
            """If the move is valid, mark the cell with an 'X'"""
            board[row][col] = 'X'

            """Print out the current state of board"""
            print_board()

            """Check if the player has won"""
            if check_win('X'):
                print("You win!")
                return

            """Check if this game is a draw"""
            if ' ' not in [cell for row in board for cell in row]:
                print("Draw!")
                return
        else:
            print("That cell is already taken.")
            continue

        """If this game is not over, AI can make a move"""
        row, col = get_ai_move()
        board[row][col] = 'O'

        """Print out the current state of board"""
        print_board()
        #Check if the AI has won
        if check_win('O'):
            print("You lose!")
            return
        #Check this game is a draw
        elif ' ' not in [cell for row in board for cell in row]:
            print("Draw!")
            return

    

if __name__ == "__main__":
    play_game()


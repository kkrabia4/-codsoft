import math

# Constants for the players
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def game_over(board):
    return check_winner(board, HUMAN_PLAYER) or check_winner(board, AI_PLAYER) or all(all(cell != EMPTY for cell in row) for row in board)

def evaluate(board):
    if check_winner(board, AI_PLAYER):
        return 1
    elif check_winner(board, HUMAN_PLAYER):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if game_over(board):
        return evaluate(board)
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_PLAYER
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    current_player = HUMAN_PLAYER
    while not game_over(board):
        print_board(board)
        if current_player == HUMAN_PLAYER:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] != EMPTY:
                print("Cell is not empty. Try again.")
                continue
            board[row][col] = HUMAN_PLAYER
        else:
            row, col = get_best_move(board)
            board[row][col] = AI_PLAYER
            print(f"AI plays at {row}, {col}")

        current_player = HUMAN_PLAYER if current_player == AI_PLAYER else AI_PLAYER

    print_board(board)
    if check_winner(board, HUMAN_PLAYER):
        print("Congratulations! You win!")
    elif check_winner(board, AI_PLAYER):
        print("AI wins! Better luck next time!")
    else:
        print("It's a tie!")

play_game()

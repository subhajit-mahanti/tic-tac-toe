import random

def display_board(board):
    index = 1
    
    for i in range(0,5):
        if i % 2 == 0:
            print(f"| {board[index]} | {board[index+1]} | {board[index+2]} |")
            index = index + 3
        else:
            print("---"*4)

def player_input():
    choice = 'Invalid'
    
    while choice not in ['X','O']:
        choice = input("Player 1, please enter your choice (X or O): ")
        
        if choice not in ['X', 'O']:
            print("Invalid choice")
            
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    # HORIZONTAL CONDITIONS
    if board[1] == mark and board[2] == mark and board[3] == mark or board[4] == mark and board[5] == mark and board[6] == mark or board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    
    # VERTICAL CONDITIONS
    elif board[1] == mark and board[4] == mark and board[7] == mark or board[2] == mark and board[5] == mark and board[8] == mark or board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    
    # DIAGONAL CONDITIONS
    elif board[1] == mark and board[5] == mark and board[9] == mark or board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    
    else:
        return False

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    else:
        return True

def player_choice(board, turn):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input(f'{turn}, choose your next position: (1-9) '))
        
    return position

def replay():
    return input('Do you want to play again? (Yes or No) ').lower().startswith('y')

print("Welcome to Tic Tac Toe")

while True:
    board = [' '] * 10
    p1_marker, p2_marker = player_input() 
    turn = choose_first()
    check_win = check_board = False

    print(f"{turn} will go first.")

    while check_win == False or check_board == False:
        if turn == 'Player 1':
            display_board(board)
            if full_board_check(board):
                print("The game was tied.")
                check_board = True
                display_board(board)
                break
            position = player_choice(board, turn)
            place_marker(board, p1_marker, position)
            if win_check(board, p1_marker):
                print(f"{turn} has won the game!")
                check_win = True
                display_board(board)
                break
            turn = 'Player 2'
            
        if turn == 'Player 2':
            display_board(board)
            if full_board_check(board):
                print("The game was tied.")
                check_board = True
                display_board(board)
                break
            position = player_choice(board, turn)
            place_marker(board, p2_marker, position)
            if win_check(board, p2_marker):
                print(f"{turn} has won the game!")
                check_win = True
                display_board(board)
                break
            turn = 'Player 1'
            
    if not replay():
        break
### 1
def display_board(board):
    print(board[1] + "l" + board[2] + 'l' + board[3])
    print(board[4] + "l" + board[5] + 'l' + board[6])
    print(board[7] + "l" + board[8] + 'l' + board[9])

### 2
def player_input():
    marker = ""
    while marker != "o" and marker != "x":
        marker = input("player 1 please choose your marker (o or x): ")
    
    player1 = marker
    if player1 == "o":
        player2 = "x"
    else:
        player2 = "o"

    return player1, player2

### 3
def marking(board,marker,position):
    board[position] = marker

### 4
def win_check(board, marker):
    #Horizontally check
    if board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker or board[7] == board[8] == board[9] == marker:
        return True
    #Vertically check
    elif board[1] == board[4] == board[7] == marker or board[2] == board[5] == board[8] == marker or board[3] == board[6] == board[9] == marker:
        return True
    #Diagonally check
    elif board[1] == board[5] == board[9] == marker or board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False

### 5
import random
def choose_first_player_random():
    first_pick = random.randint(0,1)
    
    if first_pick == 0:
        return'player1'
    else:
        return'player2'

### 6
def space_check(board, position):
    if board[position] != "o" and board[position] != "x":
        return True
    return False

### 7
def full_board_check(board):
    for item in range(1,10):
        if space_check(board, item):
            return False
    return True

### 8
def next_position_check(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):
        position = int(input('choose 1 to 9: '))
        break
    return position

### 9
def replay():
    choice = input('play game? (Y/N): ')
    if choice == "Y":
        return True
    else:
        return False

### 10
while True:
    the_board = ["0",'1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = player_input()
    first_player = choose_first_player_random()
    print(first_player + " will start first")
    play_game = input('ready to play? (Y/N): ')
    
    if play_game == "Y":
        game_on = True
    else:
        game_on = False
            
    while game_on:
        
        if first_player == 'player1':
            print("turn: " + first_player)
            display_board(the_board)
            position = next_position_check(the_board)
            marking(the_board, player1_marker, position)
            
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('player1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('draw')
                    game_on = False
                else:
                    first_player = 'player2'
                    
             
        else:
            if first_player == 'player2':
                print("turn: " + first_player)
                display_board(the_board)
                position = next_position_check(the_board)
                marking(the_board, player2_marker, position)
                
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('player2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('draw')
                        game_on = False
                    else:
                        first_player = 'player1'
                        
    if not replay():
        break

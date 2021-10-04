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
player1, player2 = player_input()

### 4
def marking(board,marker,position):
    board[position] = marker

### 5
def win_check(board, marker):
    for m in marker:
        if board[1] == board[2] == board[3] == m or board[4] == board[5] == board[6] == m or board[7] == board[8] == board[9] == m:
            return True
        elif board[1] == board[4] == board[7] == m or board[2] == board[5] == board[8] == m or board[3] == board[6] == board[9] == m: 
            return True
        elif board[1] == board[5] == board[9] == m or board[3] == board[5] == board[7] == m:
            return True
        else:
            return False

### 6
import random
def who_go_first():
    go_first = random.randint(0,1)
    
    if go_first == 0:
        return'player1'
    else:
        return'player2'

### 7
def space_check(board, position):
    if board[position] != "o" and board[position] != "x":
        return True
    return False

### 8
def full_board_check(board):
    for item in range(1,10):
        if space_check(board, item):
            return False
    return True

### 9
def next_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose 1 to 9: '))
        break
    return position

### 10
def replay():
    choice = input('play game? (Y/N): ')
    if choice == "Y":
        return True
    else:
        return False

### 11
while True:
    the_board = ["0",'1','2','3','4','5','6','7','8','9']
    player1_mark, player2_mark = player_input()
    turn = who_go_first()
    print(turn + " will go first")
    play_game = input('ready to play? (Y/N): ')
    
    if play_game == "Y":
        game_on = True
    else:
        game_on = False
            
    while game_on:
        
        if turn == 'player1':
            print("turn: " + turn)
            display_board(the_board)
            position = next_position(the_board)
            marking(the_board, player1_mark, position)
            
            if win_check(the_board, player1_mark):
                display_board(the_board)
                print('player1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('draw')
                    game_on = False
                else:
                    turn = 'player2'
                    
             
        else:
            if turn == 'player2':
                print("turn: " + turn)
                display_board(the_board)
                position = next_position(the_board)
                marking(the_board, player2_mark, position)
                
                if win_check(the_board, player2_mark):
                    display_board(the_board)
                    print('player2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('draw')
                        game_on = False
                    else:
                        turn = 'player1'
                        
    if not replay():
        break

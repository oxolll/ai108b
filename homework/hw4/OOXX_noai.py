import random
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def copy_board(board):
    copyboard = []
    for i in board:
        copyboard.append(i)
    return copyboard
def input_icon():
    icon=''
    if not (icon=='O' or icon=='X'):
        print('Choose one icon O(first) or X(second) for you')
        icon=input().upper()
    if icon=='O':
        return ['O','X','player']
    else:
        return ['X','O','computer']
def player_move(board):
    move=' '
    while True:
        print('Choose one for your next step(1-9)')
        move = input()
        for i in range(8):
            #print(move,i)
            if move == i+2:
                break
        break
    return int(move) 
def random_move(board, move_list):
    possible_move = []
    for i in move_list:
        if check_free(board, i):
            possible_move.append(i)
    if len(possible_move) != 0:
        return random.choice(possible_move)
    else:
        return None
def computer_move(board, c_icon):
    for i in range(1, 10):
        copy = copy_board(board)
        if check_free(copy, i):
            move_(copy, c_icon, i)
            if check_winner(copy, c_icon):
                return i
    for i in range(1, 10):
        copy = copy_board(board)
        if check_free(copy, i):
            move_(copy, p_icon, i)
            if check_winner(copy, p_icon):
                return i
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if check_free(board, 5):
        return 5
    return random_move(board, [2, 4, 6, 8])
def move_(board, icon, move):
    board[move] = icon
def check_winner(board, icon):
     return ((board[7] == icon and board[8] == icon and board[9] == icon) or 
            (board[4] == icon and board[5] == icon and board[6] == icon) or 
            (board[1] == icon and board[2] == icon and board[3] == icon) or 
            (board[7] == icon and board[4] == icon and board[1] == icon) or 
            (board[8] == icon and board[5] == icon and board[2] == icon) or 
            (board[9] == icon and board[6] == icon and board[3] == icon) or  
            (board[7] == icon and board[5] == icon and board[3] == icon) or  
            (board[9] == icon and board[5] == icon and board[1] == icon))
def check_space(board):
    for i in range(1, 10):
        if check_free(board, i):
            return False
    return True
def check_free(board, move):
    return board[move] == ' '
def again():
    print('Play again?(y or n)')
    return input().lower().startswith('y')
while True:
    theboard=[' ']*10
    p_icon, c_icon, turn = input_icon()
    sett = True
    while sett:
        if turn == 'player':
            drawBoard(theboard)
            move = player_move(theboard)
            move_(theboard, p_icon, move)
            if check_winner(theboard, p_icon):
                drawBoard(theboard)
                print('You win!')
                sett = False
            else:
                if check_space(theboard):
                    drawBoard(theboard)
                    print('Game is over')
                    break
                else:
                    turn = 'computer'
        else:
            move = computer_move(theboard, c_icon)
            move_(theboard, c_icon, move)
            if check_winner(theboard, c_icon):
                drawBoard(theboard)
                print('You lose!')
                sett = False
            else:
                if check_space(theboard):
                    drawBoard(theboard)
                    print('Game is over')
                    break
                else:
                    turn = 'player'
    if not again():
        break
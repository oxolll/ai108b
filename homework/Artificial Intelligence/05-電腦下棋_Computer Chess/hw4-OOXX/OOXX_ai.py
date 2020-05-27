from random import choice
from math import inf as infinity

P = +1
C = -1
def drawBoard(board, c_icon, p_icon):
    chars = {
        0:' ',
        +1: p_icon,
        -1: c_icon
    }
    for i in range(3):
        if i == 0:
            print('   |   |')
            symbol1 = chars[board[i]]
            symbol2 = chars[board[i+1]]
            symbol3 = chars[board[i+2]]
            print(' ' + f'{symbol1}' + ' | ' + f'{symbol2}' + ' | ' + f'{symbol3}')
            print('   |   |')
            print('-----------')
        elif i == 1:
            print('   |   |')
            symbol1 = chars[board[i+2]]
            symbol2 = chars[board[i+3]]
            symbol3 = chars[board[i+4]]
            print(' ' + f'{symbol1}' + ' | ' + f'{symbol2}' + ' | ' + f'{symbol3}')
            print('   |   |')
            print('-----------')
        elif i == 2:
            print('   |   |')
            symbol1 = chars[board[i+4]]
            symbol2 = chars[board[i+5]]
            symbol3 = chars[board[i+6]]
            print(' ' + f'{symbol1}' + ' | ' + f'{symbol2}' + ' | ' + f'{symbol3}')
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
        return ['O', 'X','player']
    else:
        return ['X', 'O','computer']
def player_move(board):
    move=''
    setter=0
    while True:
        print('Choose one for your next step(1-9)')
        move = input()
        cells=[]
        cells=check_free(theboard)
        for i in cells:
            #print(i)
            #print(cells)
            #print(move)
            #print(move,i)
            if int(move) == i+1:
                setter=1
                break
        #print(setter)
        #print('here')
        if setter==1:
            break
    return int(move)-1
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
def move_(move, icon):
    if valid_move(move):
        theboard[move] = icon
        return True
    else:
        return False
def valid_move(move):
    if move in check_free(theboard):
        return True
    else:
        return False

def check_winner(board, icon):
     return ((board[6] == icon and board[7] == icon and board[8] == icon) or 
            (board[3] == icon and board[4] == icon and board[5] == icon) or 
            (board[0] == icon and board[1] == icon and board[2] == icon) or 
            (board[6] == icon and board[3] == icon and board[0] == icon) or 
            (board[7] == icon and board[4] == icon and board[1] == icon) or 
            (board[8] == icon and board[5] == icon and board[2] == icon) or  
            (board[6] == icon and board[4] == icon and board[2] == icon) or  
            (board[8] == icon and board[4] == icon and board[0] == icon))
def game_over(state):
    return check_winner(state, P) or check_winner(state, C)
def evaluate(state):
    if check_winner(state, C):
        score = +1
    elif check_winner(state, P):
        score = -1
    else:
        score = 0
    return score
def minimax(state, depth, player):
    if player == C:
        best = [-1, -infinity]
    else :
        best = [-1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, score]

    for cell in check_free(state):
        
        state[cell] = player
        score = minimax(state, depth-1, -player)
        state[cell] = 0
        score[0] = cell

        if player == C:
            if score[1] > best[1]:
                best = score
        elif player == P:
            if score[1] < best[1]:
                best = score

    return best
def ai_turn(c_icon, p_icon):
    depth = len(check_free(theboard))
    if depth == 0 or game_over(theboard):
        return
    
    print(f'computer turn [{c_icon}]')
    drawBoard(theboard, c_icon, p_icon)

    if depth == 9:
        i = choice([0,1,2,3,4,5,6,7,8])
    else:
        move = minimax(theboard, depth, C)
        i = move[0]

    move_(i, C)
def check_space(board):
    for i in range(9):
        if board[i] == 0:
            return False
    return True
def check_free(state):
    cells = []
    
    for i in range(9):
        if state[i] == 0:
            cells.append(i)
    return cells
def again():
    print('Play again?(y or n)')
    return input().lower().startswith('y')
while True:
    theboard=[0]*9
    p_icon, c_icon, turn = input_icon()
    sett = True
    while sett:
        if turn == 'player':
            drawBoard(theboard, c_icon, p_icon)
            move = player_move(theboard)
            move_(move, P)
            if check_winner(theboard, P):
                drawBoard(theboard, c_icon, p_icon)
                print('You win!')
                sett = False
            else:
                if check_space(theboard):
                    drawBoard(theboard, c_icon, p_icon)
                    print('Game is over')
                    break
                else:
                    turn = 'computer'
        else:
            ai_turn(c_icon, p_icon)
            print(f'Your turn! [{p_icon}]')
            #move_(theboard, c_icon, move)
            if check_winner(theboard, C):
                drawBoard(theboard, c_icon, p_icon)
                print('You lose!')
                sett = False
            else:
                if check_space(theboard):
                    drawBoard(theboard, c_icon, p_icon)
                    print('Game is o2ver')
                    break
                else:
                    turn = 'player'
    if not again():
        break
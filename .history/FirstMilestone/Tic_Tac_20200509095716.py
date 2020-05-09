board = ['']*10

def display_board(board):
    
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
#display_board(board)

player1 = ''
player2 = ''

def player_input():
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = input('Player 1, choose x or o: ')
    
    player1 = marker
    if player1 =='x':
        player2 = 'o'
    else:
        player2 = 'x'

def place_marker(board, marker, position):
    board[position] = marker
    
place_marker(board,'$',8)
place_marker(board,'$',1)
place_marker(board,'$',5)

display_board(board)

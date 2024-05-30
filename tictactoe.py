#!/usr/bin/python
import time
import random

def print_board(board):
    
    print('---Current Game---')
    print(f'\n   {board[0]} | {board[1]} | {board[2]} ')
    print('---------------')
    print(f'   {board[3]} | {board[4]} | {board[5]} ')
    print('---------------')
    print(f'   {board[6]} | {board[7]} | {board[8]} \n')
    
    return board
 
def player_choice(board):
    choice = int(input('Choose position, between 1 - 9: '))
    
    if choice in range(1,10) and board[choice-1]  == '-':
        board[choice-1] = player
    else:
        print('Already selected, try again...')
        player_choice(board)
    time.sleep(0.3)

def computer_choice(board):
    choice = random.randint(1,9)
    
    print('Computer is choosing..\n')
    time.sleep(1)
    
    if board[choice-1] == '-':
        board[choice-1] = computer
    else:
        computer_choice(board)

def check_horizontal_win(board):
    if board[0] == board[1] == board[2] and board[1] != '-':
        print('-----Game Over-----')
        print(f'{board[1]} wins!')
        quit()
    elif board[3] == board[4] == board[5] and board[4] != '-':
        print('-----Game Over-----')
        print(f'{board[4]} wins!')
        quit()
    elif board[6] == board[7] == board[8] and board[7] != '-':
        print('-----Game Over-----')
        print(f'{board[7]} wins!')
        quit()
        
def check_vertical_win(board):
    if board[0] == board[3] == board[6] and board[3] != '-':
        print('-----Game Over-----')
        print(f'{board[3]} wins!')
        quit()
    elif board[1] == board[4] == board[7] and board[4] != '-':
        print('-----Game Over-----')
        print(f'{board[4]} wins!')
        quit()
    elif board[2] == board[5] == board[8] and board[5] != '-':
        print('-----Game Over-----')
        print(f'{board[5]} wins!')
        quit()

def check_diagonal_win(board):
    if board[0] == board[4] == board[8] and board[4] != '-':
        print('-----Game Over-----')
        print(f'{board[4]} wins!')
        quit()
    elif board[2] == board[4] == board[6] and board[4] != '-':
        print('-----Game Over-----')
        print(f'{board[4]} wins!')
        quit()

board  = ['-', '-', '-',
          '-', '-', '-',
          '-', '-', '-']

player = 'X'
computer = 'O'
playing = True

ans = input(f'-----Tic-Tac-Toe-----\n\nFeeling lucky?\n \nY = Play N = Exit: ')

if ans.lower() == 'n':
    print('Goodbye...')
    playing = False            
elif ans.lower() == 'y':
    print('\nYou are: X\n\nGame On!') 
    print_board(board)
    
while playing:
    
    player_choice(board)
    time.sleep(0.3)
    print_board(board)
    check_horizontal_win(board)
    check_vertical_win(board)
    check_diagonal_win(board)
    time.sleep(0.4)
    
    computer_choice(board)
    time.sleep(0.4)
    print_board(board)
    check_horizontal_win(board)
    check_vertical_win(board)
    check_diagonal_win(board)
    time.sleep(0.4)
    

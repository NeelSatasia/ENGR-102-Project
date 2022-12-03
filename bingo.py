# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Neel Satasia
#               Neo Kumar
#               Rithvik Rajiv
#               Shankar Jayaprakash
# Section:      510
# Assignment:   Bingo (Final Project)
# Date:         12/01/2022

import turtle
import random

'''my_window = turtle.Screen() 
my_window.bgcolor("blue")
my_pen = turtle.Turtle()      
my_pen.forward(150)           
my_pen.left(90)               
my_pen.forward(75)
my_pen.color("white")
my_pen.pensize(12)'''

def instructions():
    print('Before starting the game:')
    print('\n\tFor this program, only two users can play this game.')
    print('\tWhen manually entering numbers on the board (5x5), use comma to enter numbers for each row')
    print('\tFor example: 54,2,68,10,9 for row 1')
    
    print('\nWhile playing the game:')
    print('\n\tEach time a random number from the board will be drawn.')
    print('\tAfter a number is drawn, players will mark that number on their boards.')
    print('\tIf a player gets a bingo, then that player is the winner.')
    print("\tHowever, if both players get bingo at the same time, then it's a draw")
    print()

instructions()

#players' name
player1_name = input('Player 1 Name: ')
player2_name = input('Player 2 Name: ')
print()

board_type = ''

#asks whether or not to have random numbers on the board
while True:
    try:
        type_of_board = input('Enter 1 to have random numbers on board or 2 to type them out: ')

        if int(type_of_board) == 1 or int(type_of_board) == 2:
            board_type = int(type_of_board)
            break
        else:
            print('\n\tMust enter 1 or 2!\n')
    
    except:
        print('\n\tMust enter 1 or 2!\n')

#creates a board with random computer generated numbers
def create_rand_board():
    nums = []
    for i in range(100):
        nums.append(i)

    for j in range(24):
        rand_index = random.randint(0, len(nums) - 1)
        rand_num = nums[rand_index]
        nums.pop(rand_index)

    random.shuffle(nums)

    board = []

    for i in range(5):
        board.append([])

        for j in range(5):
            board[i].append('')
            if i == 2 and j == 2:
                board[i][j] = 'x '
            else:
                if nums[0] < 10:
                    board[i][j] = str(nums[0]) + ' '
                else:
                    board[i][j] = str(nums[0])

                nums.pop(0)

    return board

#prints the board
def print_board(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if j == len(b) - 1:
                print(b[i][j], end='')
            else:
                print(b[i][j], end=' ')
        print('\n')

        
#shuffles a board
def shuffle_board(b):
    nums = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            nums.append(b[i][j])

    nums.remove('x ')

    random.shuffle(nums)
    
    randomized_b = []

    for i in range(len(b)):
        randomized_b.append([])

        for j in range(5):
            randomized_b[i].append('')

            if i == 2 and j == 2:
                randomized_b[i][j] = '+ '
            else:
                randomized_b[i][j] = nums[0]
                nums.pop(0)
    
    return randomized_b    

player1_board = []
player2_board = []

#checks if the players want random numbers
if board_type == 1:
    new_rand_board = create_rand_board()
    player1_board = new_rand_board
    print(f"\n{player1_name}'s board:\n")
    print_board(new_rand_board)
    
    print(f"\n{player2_name}'s board:\n")
    shuffled_board = shuffle_board(new_rand_board)
    player2_board = shuffled_board
    print_board(shuffled_board)

elif board_type == 2:
    row = 1

    manual_board = []
    
    while True:
        nums_input = input('Row ' + str(row) + ' (use commas without spaces): ')

        row_nums = nums_input.split(',')

        error = False

        try:
            
            #using sets to detect any duplicates
            nums_set = set(())

            for value in row_nums:
                nums_set.add(value)

            #checks if length of the set is less than that of row_nums
            if len(nums_set) < len(row_nums):
                error = True
            
            if error == False:
                for k in range(len(row_nums)):
                    if row_nums[k] != 'x' and row != 3:
                        row_nums[k] = int(row_nums[k])

                        for i in range(len(manual_board)):
                            for j in range(len(manual_board[i])):
                                if i != 2 or j != 2:
                                    n = int(manual_board[i][j].strip())

                                    if n == row_nums[k]:
                                        error = True
                                        break
                                elif manual_board[i][j] != 'x ':
                                    error = True
                                    break
                                

            if error == False:
                manual_board.append([])

                for i in range(5):
                    if row == 3 and i == 2:
                        manual_board[-1].append('x ')
                    elif int(row_nums[i]) < 10:
                        manual_board[-1].append(str(row_nums[i]) + ' ')
                    else:
                        manual_board[-1].append(str(row_nums[i]))

                row += 1
            else:
                print('\n\tDuplicates not allowed!\n')
                row = 1
                manual_board = []

        except:
            row = 1
            manual_board = []
            print('\n\tInvalid Input!\n')

        if row > 5:
            player1_board = manual_board
            break


while True:
    is_shuffle = input('Do you want to shuffle it (y or n): ')

    if is_shuffle == 'y':
        try:
            
        

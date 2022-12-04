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
    '''Prints the instructions of how to play the game and use the program'''
    
    print('Before starting the game:')
    print('\n\tFor this program, only two users can play this game.')
    print('\tWhen manually entering numbers on the board (5x5), use comma to enter numbers for each row')
    print('\tFor example: 54,2,68,10,9 for row 1')
    print("\tDon't forget to put x in row 3 column 3 which is in the center of the board")
    
    print('\nWhile playing the game:')
    print('\n\tEach time a random number from 0-99 will be drawn.')
    print('\tAfter a number is drawn, players will mark that number on their boards.')
    print('\tIf a player gets a bingo, then that player is the winner.')
    print("\tHowever, if both players get bingo at the same time, then it's a draw")
    print()

instructions()

#gets data of the scores from the file
def get_data():
    file = open('bingodata.txt', 'r')

    scores = []

    for line in file.readlines():
        scores.append(line.strip())

    return scores

file_data = get_data()

#players' name
player1_name = input('Player 1 Name: ')
player2_name = input('Player 2 Name: ')
print()

board_type = ''

#asks whether or not to have random numbers on the board
while True:
    try:
        type_of_board = input('Enter 1 to have random numbers on board or 2 to type them out: ')
        print()

        if int(type_of_board) == 1 or int(type_of_board) == 2:
            board_type = int(type_of_board)
            break
        else:
            print('\n\tMust enter 1 or 2!\n')
    
    except:
        print('\n\tMust enter 1 or 2!\n')

#creates a board with random computer generated numbers
def create_rand_board():
    '''Creates a 5x5 board with random numbers including the x in the middle'''
    
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
    '''This function prints the bingo board on the console'''
    
    for i in range(len(b)):
        for j in range(len(b[i])):
            if j == len(b) - 1:
                print(b[i][j], end='')
            else:
                print(b[i][j], end=' ')
        print('\n')

        
#shuffles a board
def shuffle_board(b):
    '''This function shuffles a given board'''
    
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
                randomized_b[i][j] = 'x '
            else:
                randomized_b[i][j] = nums[0]
                nums.pop(0)
    
    return randomized_b

#saves data in the file
def save_data(player1_n, player2_n, winner):
    file = open('bingodata.txt', 'w')
    names_exist = False
    
    for line in file_data:
        players_data = line.split(', ')
        
        p1_name = players_data[0].split(': ')[0]
        p2_name = players_data[1].split(': ')[0]
        
        player1_score = int(players_data[0].split(': ')[1])
        player2_score = int(players_data[1].split(': ')[1].strip())
        
        if player1_n == p1_name and player2_n == p2_name:
            names_exist = True

            if winner == 1:
                player1_score += 1
            elif winner == 2:
                player2_score += 1
            
            file.write(player1_n + ': ' + str(player1_score) + ', ' + player2_n + ': ' + str(player2_score) + '\n')

        else:
            file.write(line + '\n')
            
    file.close()

    if names_exist == False:
        
        file = open('bingodata.txt', 'a')
        
        if winner == 1:
            file.write(f"{player1_n}: 1, {player2_n}: 0")
        elif winner == 2:
            file.write(f"{player1_n}: 0, {player2_n}: 1")
        else:
            file.write(f"{player1_n}: 0, {player2_n}: 0")

        file.close()


def is_bingo(b):
    '''This function checks if a given board got a bingo.'''
    
    arr = []

    for i in range(len(b)):
        arr.append(b[i])

    for i in range(len(b)):
        arr.append([])
        for j in range(len(b[i])):
            arr[-1].append(b[j][i])

    # for the diagonals
    arr.append([])
    arr.append([])

    for i in range(len(b)):
        for j in range(len(b[i])):
            if i == j:
                arr[-2].append(b[i][j])

            if len(b[i]) - 1 - i == j:
                arr[-2].append(b[i][j])

    for i in range(len(arr)):
        new_set = set(())

        for j in range(len(arr[i])):
            new_set.add(arr[i][j])

        if len(new_set) == 1:
            return True

    return False


player1_board = []
player2_board = []

#checks if the players want random numbers
if board_type == 1:
    p1_rand_board = create_rand_board()
    player1_board = p1_rand_board
    
    p2_rand_board = create_rand_board()
    player2_board = p2_rand_board

elif board_type == 2:
    row = 1

    manual_board = []

    player1_done = False
    player2_done = False

    print(f"{player1_name}'s board:\n")
    
    while True:
        nums_input = input('Row ' + str(row) + ' (use commas without spaces): ')

        row_nums = nums_input.split(',')

        error = False

        board_row_size = len(manual_board)

        try:
            
            #using sets to detect any duplicates
            nums_set = set(())

            for value in row_nums:
                nums_set.add(value)

            #checks if length of the set is less than that of row_nums
            if len(nums_set) < len(row_nums):
                error = True

            if error == False:
                if row == 3 and row_nums[2] != 'x':
                    error = True
            
            if error == False:
                for k in range(5):
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
                print('\n\tDuplicates not allowed and must put an x at row 3 column 3!\n')

        except:
            if len(manual_board) > board_row_size:
                manual_board[-1] = []
            print('\n\tInvalid Input!\n')

        if row > 5:
            player1_board = manual_board

            if player1_done == False:
                player1_done = True
                row = 1
                manual_board = []
                print(f"\n{player2_name}'s board:\n")
            else:
                player2_done = True
                player2_board = manual_board
                break


    while True:
        is_shuffle = input('\nDo you want to shuffle it (y or n): ')

        if is_shuffle == 'y':
            player1_board = shuffle_board(player1_board)
            player2_board = shuffle_board(player2_board)
            break

        elif is_shuffle == 'n':
            print('\nThe game begins!\n')
            break

        else:
            print('\n\tMust enter y or n!\n')

        
print(f"{player1_name}'s board:\n")
print_board(player1_board)

print(f"\n{player2_name}'s board:\n")
print_board(player2_board)

nums = []

for i in range(100):
    nums.append(i)



while True:
    draw_num = input('Press enter to pick a random number: ')

    rand_index = random.randint(0, len(nums) - 1)
    drawn_num = nums[rand_index]
    nums.pop(rand_index)

    print(f"\nDrawn Number: {drawn_num}")

    p1_num_exists = False
    p2_num_exists = False

    for i in range(len(player1_board)):
        for j in range(len(player1_board[i])):
            
            if player1_board[i][j] != 'x ' and int(player1_board[i][j].strip()) == drawn_num:
                player1_board[i][j] = 'x '
                p1_num_exists = True

            if player2_board[i][j] != 'x ' and int(player2_board[i][j].strip()) == drawn_num:
                player2_board[i][j] = 'x '
                p2_num_exists = True

    if p1_num_exists == True:
        print(f"\n{player1_name}'s board:\n")
        print_board(player1_board)
    else:
        print(f"\n{player1_name}'s board doesn't have the drawn number!")
        
    if p2_num_exists == True:
        print(f"\n{player2_name}'s board:\n")
        print_board(player2_board)
    else:
        print(f"{player2_name}'s board doesn't have the drawn number!")

    if is_bingo(player1_board) == True and is_bingo(player2_board) == False:
        print('\n-----------BINGO!-----------\n')
        print(f"{player1_name} won!")
        winner = 1
        save_data(player1_name, player2_name, winner)
        break

    elif is_bingo(player2_board) == True and is_bingo(player1_board) == False:
        print('\n-----------BINGO!-----------\n')
        print(f"{player2_name} won!")
        winner = 2
        save_data(player1_name, player2_name, winner)
        break

    elif is_bingo(player1_board) == True and is_bingo(player2_board) == True:
        print(f"It's a draw!")
        winner = 3
        save_data(player1_name, player2_name, winner)
        break

    else:
        print()


        

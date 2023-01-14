# 1) Candy grab game (human vs human and human vs robot)
print('\nTask 1')
print('------\n')
from random import randint

def grab_candy(name):
    x = int(input(f'{name}, enter a number of candies (1..28): '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, enter a correct number: '))
    return x

def show_status(name, k, counter, value):
    print(f'{name} turn, he takes {k}, he has {counter} in total. {value} candies are left on the table.')

def game_with_human():
    player1 = input('Enter a name of 1st player: ')
    player2 = input('Enter a name of 2nd player: ')
    value = int(input('Enter a number of candies on the table: '))
    flag = randint(0, 2)  # who is the first
    if flag:
        print(f'The first turn is for {player1}')
    else:
        print(f'The first turn is for {player2}')

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = grab_candy(player1)
            counter1 += k
            value -= k
            flag = False
            show_status(player1, k, counter1, value)
        else:
            k = grab_candy(player2)
            counter2 += k
            value -= k
            flag = True
            show_status(player2, k, counter2, value)

    if flag:
        print(f'{human} wins')
    else:
        print(f'{robot} wins')

def game_with_robot():
    human = input('Enter a name of the human: ')
    robot = input('Enter a name of the robot: ')
    value = int(input('Enter a number of candies on the table: '))
    flag = randint(0, 2)  # who is the first
    if flag:
        print(f'The first turn is for {human}')
    else:
        print(f'The first turn is for {robot}')

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = grab_candy(human)
            counter1 += k
            value -= k
            flag = False
            show_status(human, k, counter1, value)
        else:
            if value > 57:
                k = randint(1, 29)
                counter2 += k
                value -= k
                flag = True
            elif 28 < value < 57:    
                k = 1
                counter2 += k
                value -= k
                flag = True  
            elif value < 29:    
                k = value
                counter2 += k
                value -= k
                flag = True            
            show_status(robot, k, counter2, value)

    if flag:
        print(f'{human} wins')
    else:
        print(f'{robot} wins')

# game_with_human() 
# game_with_robot()       


# 2) Tic-Tac-Toe Game
print('\nTask 2')
print('------\n')

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# main function which has all the gameplay functionality
def tic_tac_toe_game():

    theBoard = {
        '7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' 
    }

    board_keys = []

    for key in theBoard:
        board_keys.append(key)

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + " .Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # check if player X or O has won, for every move after 5 moves 
        if count >= 5:
            
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")                
                break
            
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break
            
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break
            
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break
            
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break
            
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break
            
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
                break 

        # if neither X nor O wins and the board is full, the result is declared as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # ask if player wants to restart the game or not.
    restart = input("Do want to play again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        tic_tac_toe_game()
    else:
        print()       

# tic_tac_toe_game()


# 3) Run-length encoding
print('\nTask 3')
print('------\n')

def encode():
    message = input('Enter a message: ')
    encoded_message = ""
    i = 0
 
    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count += 1
                j += 1
            else:
                break
        
        encoded_message = encoded_message + str(count) + ch
        i = j + 1
    
    print(f'Encoded massage: {encoded_message}\n')
    
encode() 

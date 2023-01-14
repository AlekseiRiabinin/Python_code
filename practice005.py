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
game_with_robot()       


# 1b) Candy grab game (human vs bot)
print('\nTask 1')
print('------\n')
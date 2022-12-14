
# 1) Write a program that takes a number as an input representing the day of the week 
# and checks whether that day is week
print('Task 1')
print('------\n')
def day_checker():
    weekday = int(input('Enter any weekday number (1-7): '))

    if weekday in range(1, 6):
        print('Weekday\n')

    elif weekday in range(6, 8):
        print('Weekend\n')

    else:
        print('Please enter any weekday number (1-7)\n')

day_checker()        


# 2) Write a program for verification of the truth of the statement 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for all values of the predicate
print('Task 2')
print('------\n')
def input_numbers(x):
    xyz = ['X', 'Y', 'Z']
    arr = []
    for i in range(x):
        arr.append(input(f'Enter the value {xyz[i]}: '))
    return arr

def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

def predicate_checker():
    x=int(input('Enter the number (<=3): '))
    
    if x > 3 or x < 0:
        print('Try again\n')
    else:
        statement = input_numbers(x=x)
    
        if check_predicate(statement) == True:
            print('Statement is true\n')
        else:
            print('Statement is false\n')

predicate_checker()


# 3) Write a program that takes coordinates of a point (X and Y) as an input, 
# with X ≠ 0 and Y ≠ 0, and outputs the quadrant of the plane 
# in which this point is located (or on which axis it is located)
print('Task 3')
print('------\n')
def quadrant(x, y):
    if (x > 0 and y > 0):
        print ('lies in First quadrant\n')
 
    elif (x < 0 and y > 0):
        print ('lies in Second quadrant\n')
         
    elif (x < 0 and y < 0):
        print ('lies in Third quadrant\n')
     
    elif (x > 0 and y < 0):
        print ('lies in Fourth quadrant\n')
         
    elif (x == 0 and y > 0):
        print ('lies at positive Y axis\n')
     
    elif (x == 0 and y < 0):
        print ('lies at negative Y axis\n')
     
    elif (y == 0 and x < 0):
        print ('lies at negative X axis\n')
     
    elif (y == 0 and x > 0):
        print ('lies at positive X axis\n')
     
    else:
        print ('lies at origin\n')
 
def quadrant_checker():
    x=float(input('Enter X-coordinate: '))
    y=float(input('Enter Y-coordinate: '))
    quadrant(x, y)

quadrant_checker()    


# 4) Write a program that, given a quadrant, shows the range of 
# possible coordinates of points in that quadrant (x and y)
print('Task 4')
print('------\n')
def range_checker():
    quad=int(input('Enter the quadrant (1, 2, 3, 4): '))
    
    if quad == 1:
        print ('x > 0 and y > 0\n')
 
    elif quad == 2:
        print ('x < 0 and y > 0\n')
         
    elif quad == 3:
        print ('x < 0 and y < 0\n')
     
    elif quad == 4:
        print ('x > 0 and y < 0\n')

    else:
        print ('Try again\n')    
 
range_checker()


# 5) Write a program that takes the coordinates of two points as an input
# and finds the distance between them in 2D space
print('Task 5')
print('------\n')
import math
def euclidean_distance():
    x1=float(input('Enter X1-coordinate: '))
    y1=float(input('Enter Y1-coordinate: '))
    x2=float(input('Enter X2-coordinate: '))
    y2=float(input('Enter Y2-coordinate: '))

    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
    print(f'Euclidean_distance: {dist}') 

euclidean_distance()
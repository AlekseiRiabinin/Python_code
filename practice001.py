
# 1) Write a program that takes a number as an input representing the day of the week 
# and checks whether that day is week
print('Task 1\n')
def day_checker():
    weekday = int(input('Enter weekday number (1-7): '))

    if weekday in range(1, 6):
        print('Weekday\n')

    elif weekday in range(6, 8):
        print('Weekend\n')

    else:
        print('Please enter any weekday number (1-7)\n')

# day_checker()        


# 2) Write a program for verification of the truth of the statement 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for all values of the predicate
print('Task 2\n')
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
        print('Try again')
    else:
        statement = input_numbers(x=x)
    
        if check_predicate(statement) == True:
            print('Statement is true')
        else:
            print('Statement is false')

# predicate_checker()


# 3) Write a program that takes the coordinates of a point (X and Y) as an input, 
# with X ≠ 0 and Y ≠ 0, and outputs the quadrant of the plane 
# in which this point is located (or on which axis it is located)
print('Task 3\n')
def quadrant(x, y):
    if (x > 0 and y > 0):
        print ('lies in First quadrant')
 
    elif (x < 0 and y > 0):
        print ('lies in Second quadrant')
         
    elif (x < 0 and y < 0):
        print ('lies in Third quadrant')
     
    elif (x > 0 and y < 0):
        print ('lies in Fourth quadrant')
         
    elif (x == 0 and y > 0):
        print ('lies at positive Y axis')
     
    elif (x == 0 and y < 0):
        print ('lies at negative Y axis')
     
    elif (y == 0 and x < 0):
        print ('lies at negative X axis')
     
    elif (y == 0 and x > 0):
        print ('lies at positive X axis')
     
    else:
        print ('lies at origin')
 
def quadrant_checker():
    x=float(input('Enter X-coordinate: '))
    y=float(input('Enter Y-coordinate: '))
    quadrant(x, y)

quadrant_checker()    
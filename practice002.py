# 1) The program takes an intager as an input and 
# displays the sum of its digits
print('\nTask 1')
print('------\n')

def int_sum():
    n = input('Enter a number: ')
    result = 0
    for i in range(len(n)):
        result += int(n[i])
    print(f'Sum of digits in the number: {result}\n')

# int_sum()    


# 2) The program generates a list of integers based on the sequence 
# (1 + 1/n)**n and displays the sum of its elements
print('\nTask 2')
print('------\n')

def seq_generator(n):
    for x in range(1, n+1):
        yield round((1 + 1/x)**x, 2)
        
def sum_calculator():
    n = int(input('Enter a number: '))
    
    arr = []
    for x in seq_generator(n):
        arr.append(x)
    print(arr)

    result = 0
    for i in arr:
        result += i
    print(f'Sum of digits in the number: {result}\n')    

# sum_calculator()    


# 3) The program shuffles a list of numbers
print('\nTask 3')
print('------\n')

import random
def list_shuffler():
    n = int(input('Enter number of elements: '))
    
    arr = []
    for i in range(n):
        x = int(input(f'Element {i+1}: '))
        arr.append(x)
    
    print(f'\nOriginal list: {arr}')
    
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]

    print(f'Shuffled list: {arr}\n')  

list_shuffler()      
    
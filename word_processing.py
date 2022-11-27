# input words
def inserter():
    print('Enter 1st word:')
    x1 = str(input())
    print('Enter 2nd word:')
    x2 = str(input())
    print('Enter 3rd word:')
    x3 = str(input())
    arr = [x1, x2, x3]
    return arr

# count symbols
def counter(inp=inserter()):
    out = []
    for x in inp:
        if len(x) <= 3:
            out.append(x)
    print('Filtered words:', out) 

# run the program
counter()
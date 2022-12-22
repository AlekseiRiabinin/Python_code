# 1) The program prints Sum of even and odd elements in an array
print('\nTask 1')
print('------\n')

def even_odd_sum():
    lst = []
    n = int(input('Enter number of elements: '))
 
    for i in range(n):
        item = int(input(f'Element {i + 1}: '))
        lst.append(item)

    even = 0
    odd = 0
    for j in range(n):
        if j % 2 == 0:
            even += lst[j]
        else:
            odd += lst[j]
     
    print (f'\nEven index positions sum: {even}' )
    print (f'Odd index positions sum: {odd}\n')
 
# even_odd_sum()


# 2) The program multiplies pairs of first - last, second - anterior to last etc.
print('\nTask 2')
print('------\n')

def reverse_list(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst    

def remove_middle(lst):
    idx = 0
    size = len(lst)
    idx = size // 2

    if (size % 2 == 1):
        lst.pop(idx)

    return lst

def multiply_pairs():
    dir_lst = []
    n = int(input('Enter number of elements: '))
 
    for i in range(n):
        item = int(input(f'Element {i + 1}: '))
        dir_lst.append(item)

    dir_lst = remove_middle(dir_lst)
    rev_lst = reverse_list(dir_lst.copy(), 0, len(dir_lst)-1)

    mul_lst = []
    for j in range(0, len(dir_lst)):
        mul_lst.append(dir_lst[j] * rev_lst[j])

    mul_lst_print = mul_lst[: len(mul_lst) // 2]

    print (f'\nOriginal list: {dir_lst}')
    print (f'Reversed list: {rev_lst}')  
    print (f'List of multiplied pairs: {mul_lst_print}\n')

multiply_pairs()


# # 3) The program shuffles a list of numbers
# print('\nTask 3')
# print('------\n')



# # 4) The program shuffles a list of numbers
# print('\nTask 4')
# print('------\n')



# # 5) The program shuffles a list of numbers
# print('\nTask 5')
# print('------\n')
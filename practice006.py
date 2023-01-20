# 1) The program prints sum of even and odd elements in an array
print('\nTask 1')
print('------\n')

def even_odd_sum():
    lst = [int(item) for item in str(input("Enter the list items: "))]
    
    even = 0
    odd = 0

    for j, k in zip(lst, lst):
        
        even_list = list(filter(lambda j: j % 2 == 0, lst))
        for e_idx, e_item in enumerate(even_list):
            even += even_list[e_idx]
        
        odd_list = list(filter(lambda k: k % 2 != 0, lst))
        for o_idx, o_item in enumerate(odd_list):
            odd += odd_list[o_idx]
    
    print (f'\nEven index positions sum: {even}')
    print (f'Odd index positions sum: {odd}\n')

even_odd_sum()


# # 2) The program multiplies pairs of array elements:
# # first - last, second - anterior to last etc.
# print('\nTask 2')
# print('------\n')

# def reverse_list(lst, start, end):
#     while start < end:
#         lst[start], lst[end] = lst[end], lst[start]
#         start += 1
#         end -= 1
    
#     return lst    

# def remove_middle(lst):
#     idx = 0
#     idx = len(lst) // 2

#     if (len(lst) % 2 == 1):
#         lst = lambda idx: lst.pop(idx)

#     return lst

# def multiply_pairs():
#     dir_lst = [int(item) for item in str(input("Enter the list items: "))]    

#     dir_lst = remove_middle(dir_lst)
#     rev_lst = reverse_list(dir_lst.copy(), 0, len(dir_lst) - 1)

#     mul_lst = []
#     for j,k in enumerate(dir_lst):
#         mul_lst.append(dir_lst[j] * rev_lst[j])

#     mul_lst_print = mul_lst[: len(mul_lst) // 2]

#     print (f'\nOriginal list having pairs: {dir_lst}')
#     print (f'List of multiplied pairs: {mul_lst_print}\n')

# # multiply_pairs()


# 3) The program extracts the fractional parts of float numbers
# and finds difference between their max and min (if value is not zero) 
print('\nTask 3')
print('------\n')
def fractional_difference():
    n = int(input('Enter number of elements: '))
    
    lst_float = []
    for i in range(n):
        item = float(input(f'Element {i + 1}: '))
        lst_float.append(item)
    
    lst_frac = []
    for j in range(n):
        frac = lst_float[j] % 1
        lst_frac.append(frac)

    lst_filtered = [x for x in lst_frac if x != 0]
    lst_sorted = sorted(lst_filtered) 

    diff = round((lst_sorted[-1] - lst_sorted[0]), 2)
    print (f'\nDifference between max and min of fractional parts: {diff}\n')

fractional_difference()
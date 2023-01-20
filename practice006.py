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


# 2) The program extracts the fractional parts of float numbers
# and finds difference between their max and min (if value is not zero) 
print('\nTask 2')
print('------\n')

def fractional_difference():
    n = int(input('Enter number of elements: '))
    
    lst_float = []
    for i in range(n):
        item = float(input(f'Element {i + 1}: '))
        lst_float.append(item)
  
    lst_frac = list(map(lambda x: x % 1, lst_float))
    lst_sorted = sorted([x for x in lst_frac if x != 0]) 

    diff = round((lst_sorted[-1] - lst_sorted[0]), 2)
    print (f'\nDifference between max and min of fractional parts: {diff}\n')
 
fractional_difference()
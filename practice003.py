# 1) The program prints Sum of even and odd elements in an array
print('\nTask 1')
print('------\n')

def even_odd_sum():
    lst = []
    n = int(input('Enter number of elements: '))
 
    for i in range(n):
        item = int(input(f'Element {i+1}: '))
        lst.append(item)

    even = 0
    odd = 0
    for j in range(n):
        if j % 2 == 0:
            even += lst[j]
        else:
            odd += lst[j]
     
    print (f'Even index positions sum: {even}' )
    print (f'Odd index positions sum: {odd}\n')
 
even_odd_sum()


# # 2) The program generates a list of integers based on the sequence 
# # (1 + 1/n)**n and displays the sum of its elements
# print('\nTask 2')
# print('------\n')



# # 3) The program shuffles a list of numbers
# print('\nTask 3')
# print('------\n')



# # 4) The program shuffles a list of numbers
# print('\nTask 4')
# print('------\n')



# # 5) The program shuffles a list of numbers
# print('\nTask 5')
# print('------\n')
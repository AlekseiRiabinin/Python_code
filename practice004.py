# 1) The program creates two polynomials with given power and random coefficients > 0
# and writes them to the output file
print('\nTask 1')
print('------\n')
import random
import pickle
from sympy import symbols

def polynomial():
    k = int(input('Enter coefficient (power): '))
    var = 'x'
    
    coefs = []
    for i in range(k + 1):
        n = random.randint(1, 100)
        coefs.append(n)  
   
    x = symbols(var)
    return sum(a * x ** k for k, a in enumerate(reversed(coefs)))

def print_polynomial():
    for i in range(1, 3):
        var = f'004_{i}' 

        print(f'Polynomial {i}')   
        poly = polynomial()
        print()
        
        f = open(f'practice{var}.txt', 'w')
        f.write(str(poly))
        f.close()   

        f = open(f'practice{var}.txt', 'a')
        f.write(' = 0')
        f.close()     
 
print_polynomial()


# # 2) The program creates polynomial with given power and random coefficients > 0
# print('\nTask 2')
# print('------\n')
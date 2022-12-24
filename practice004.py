# 1) The program creates two polynomials with given power and random coefficients > 0
# and writes them to the output txt files
print('\nTask 1')
print('------\n')
import random
from sympy import symbols

def create_polynomial(mode):
   
    if mode == 'create':
        k = int(input('Enter coefficient (power): '))
        coefs = []
        for i in range(k + 1):
            n = random.randint(1, 100)
            coefs.append(n)  

    if mode == 'extract':
        coefs = add_polynomial()

    x = symbols('x')
    return sum(a * x ** k for k, a in enumerate(reversed(coefs)))

def print_polynomial(n, mode):
    for i in range(1, n + 1):
        var = f'004_{i}' 

        if mode == 'create':
            var = f'004_{i}'

            print(f'Polynomial {i}')   
            poly = create_polynomial(mode)
            print()

            f = open(f'practice{var}.txt', 'w')
            f.write(str(poly))
            f.close()   

            f = open(f'practice{var}.txt', 'a')
            f.write(' = 0')
            f.close()     

        if mode == 'extract':
            var = f'004_{i + 2}'
            print(f'Polynomial {i + 2}')   
            poly = create_polynomial(mode)
            print()

            f = open(f'practice{var}.txt', 'w')
            f.write(str(poly))
            f.close()   

            f = open(f'practice{var}.txt', 'a')
            f.write(' = 0')
            f.close()  
 
print_polynomial(n=2, mode='create')


# 2) The program extracts polynomials from txt files, finds their sum
# and writes it to the output txt file
print('\nTask 2')
print('------\n')

def extract_polynomial(file):
    f = open(file, 'r')
    poly_original = f.read()
    size = len(poly_original)
    poly_modified = poly_original[:size - 4]
    poly_terms = poly_modified.split('+')
    
    poly_dict = {}
    for sub in poly_terms:
        values = sub.split('*')
        try:
            base = int(values[0])
            poly = '*'.join(values[1:]).strip()
        except:
            base = 1
            poly = '*'.join(values).strip()
        
        poly_dict[poly] = base 
        poly_coefs = list(poly_dict.values())

    return poly_coefs  

def add_polynomial():
    poly1 = extract_polynomial(file='practice004_1.txt')
    poly2 = extract_polynomial(file='practice004_2.txt')

    result = [sum(value) for value in zip(poly1, poly2)]
    return result

print_polynomial(n=1, mode='extract')
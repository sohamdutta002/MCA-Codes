# Write a program to compute cosine of x. The user should supply x and a positive integer n. We compute the cosine of x using the series and the computation should use all terms in the series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....

def cos_x(x, n):
    cosx = 0
    for i in range(1, n+1):
        cosx += ((-1)**(i-1))*(x**(2*i-2))/math.factorial(2*i-2)
    return cosx

import math
x = int(input('Enter the value of x: '))
n = int(input('Enter the value of n: '))
print(cos_x(x, n))
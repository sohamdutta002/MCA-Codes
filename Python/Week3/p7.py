# Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........

def sin_x(x, n):
    sinx = 0
    for i in range(1, n+1):
        sinx += ((-1)**(i-1))*(x**(2*i-1))/math.factorial(2*i-1)
    return sinx

import math
x = int(input('Enter the value of x: '))
n = int(input('Enter the value of n: '))
print(sin_x(x, n))
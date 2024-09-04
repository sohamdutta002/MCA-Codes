# Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.

def sum_series(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum -= 1/i
        else:
            sum += 1/i
    return sum

n = int(input('Enter the value of n: '))
print(sum_series(n))
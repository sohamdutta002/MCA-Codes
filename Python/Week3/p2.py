# Write a function called calculate_slope which return the slope of a linear equation.

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'The slope is infinite'
    else:
        return (y2-y1)/(x2-x1)

x1 = int(input('Enter the value of x1: '))
y1 = int(input('Enter the value of y1: '))
x2 = int(input('Enter the value of x2: '))
y2 = int(input('Enter the value of y2: '))
print(calculate_slope(x1, y1, x2, y2))
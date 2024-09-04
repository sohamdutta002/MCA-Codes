# Write a function to calculate the power of a number using recursion.

def power(num,times):
    if times==0:
        return 1
    return num*power(num,times-1)

n=int(input("Enter a number : "))
t=int(input("Enter its exponent : "))
print(power(n,t))
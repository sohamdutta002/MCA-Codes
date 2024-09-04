# Find GCD of two numbers.

def gcd(a,b):
    if b==0:
        return abs(a)
    else:
        return gcd(b,a%b)

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("Their gcd is : ",gcd(a,b))
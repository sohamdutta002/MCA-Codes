# WAP to generate prime number series upto n

def checkPrime(i):
    if i in [2,3]:
        return True
    if i==1 or i%2==0:
        return False
    r=3
    while r*r<=i:
        if i%r==0:
            return False
        r+=2
    return True

n=int(input("Enter value of n : "))
for i in range(1,n):
    if checkPrime(i)==True:
        print(i)
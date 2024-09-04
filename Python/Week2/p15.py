# Write a Python program that prompts the user to enter a base number and an exponent and then calculates the power of the base to the exponent. The program should not use rhe exponentiation operatior (**) or the math.pow() function.

base=int(input("Enter base : "))
exp=int(input("Enter exponent : "))

if exp==0:
    print("1")
ans=1
while exp>0:
    ans*=base
    exp-=1
print(ans)
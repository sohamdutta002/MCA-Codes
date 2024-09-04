# Write a program in Python to check if a number is Krishnamurthy number.

num=int(input("Enter a number : "))

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
temp=num
sum=0
while(num>0):
    digit=num%10
    num//=10
    sum+=fact(digit)

if(temp==sum):
    print(temp," is a Krishnamurthy Number ...")
else:
    print("Not a Krishnamurthy Number...")
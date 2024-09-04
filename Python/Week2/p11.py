# Write a program in Python to find the sum of digits of a number.

num=int(input("Enter a number : "))
sum=0
temp=num
while num>0:
    sum+=num%10
    num//=10
print("Sum of digits of ",temp," is : ",sum)
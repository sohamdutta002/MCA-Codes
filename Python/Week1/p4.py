# WAP to display reverse of a number

num=int(input("Enter a number"))
temp=num
reverse=0
while(temp>0):
    reverse=reverse*10+temp%10
    temp=temp//10
print(f"The reverse of {num} is : {reverse}")
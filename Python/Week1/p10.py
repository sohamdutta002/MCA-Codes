# WAP to generate Fibonacci series upto n.

num=int(input("Enter value of n : "))
previous=1
present=1
while previous<num:
    print(previous),
    temp=previous
    previous=present
    present=temp+present

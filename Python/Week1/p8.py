# WAP to check whether a number is palindrome or not.

n=int(input("Enter a number : "))
temp=n
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
if rev==n:
    print("Palindrome Number !")
else:
    print("Not Palindrome ...")
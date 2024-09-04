# Convert Decimal number to Binary.

num=int(input("Enter decimal number : "))
temp=num
ans=""
while(num>0):
    digit=num%2
    num//=2
    ans+=str(digit)
reverse=ans[::-1]
print(reverse," is the binary representation of ",temp)
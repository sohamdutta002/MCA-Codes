# WAP to find factors of a given number.

num=int(input("Enter a number : "))
print(f"The factors of the number {num} are : ")
for i in range(1,num//2):
    if(num%i==0):
        print(i)
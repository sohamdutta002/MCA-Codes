# WAP to check whether a)is a perfect number b)is an Armstrong number

def perfect(num):
    sum=0
    for i in range (1,num//2):
        if(num%i==0):
            sum+=i
    
    if sum==num:
        print("Perfect Number : ",num)
    else:
        print("Not a perfect number ......")

def armstrong(num):
    sum=0
    temp=num
    length=len(str(num))
    while temp>0:
        digit=temp%10
        sum+=digit**length
        temp//=10
    if num==sum:
        print("Armstrong Number !")
    else:
        print("Not Armstrong Number !")

n=int(input("Enter a number"))
perfect(n)
armstrong(n)
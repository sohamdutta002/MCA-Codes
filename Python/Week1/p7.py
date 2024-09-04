# WAP which makes use of function to display all such numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000.

def check():
    for i in range(1000,2000):
        if i%7==0 and i%5!=0:
            print(i),

check()
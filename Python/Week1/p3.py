# WAP to check whether a given year is leap year or not

year=int(input("Enter a year : "))
if((year%400==0)or(year%4==0 and year%100!=0)):
    print(f"{year} is a leap year !")
else:
    print(f"{year} is NOT a leap year !")
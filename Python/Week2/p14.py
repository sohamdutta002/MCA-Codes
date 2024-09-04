# Print the series upto N terms: 1,2,6,24,120,720 ...

n=int(input("Enter value of n : "))
a=1
ans="1, "
for i in range(2,n+1):
    a*=i
    ans+=str(a)
    ans+=", "
print(ans)
# Write a Python program to print rhe first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.

n=6
a=2
r=3
ans=""
for i in range(1,n+1):
    ans+=str(a*(r**(i-1)))
    ans+=", "
print(ans)
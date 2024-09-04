# To solve the quadratic equation.

print("Equation like : ax^2+bx+c")
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
discriminant=(b**2-4*a*c)**(0.5)
ans1=discriminant-b
ans2=-discriminant-b
ans1/=(2*a)
ans2/=(2*a)
print(ans1," and ",ans2)
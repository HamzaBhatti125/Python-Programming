#QUADRATIC FORMULA
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
print(a,'x2+',b,"x+",c,"=0",sep="")
d=(b**2)-(4*a*c)
e=(d**0.5)/(2*a)
f=-b/(2*a)
x1=f+e
x2=f-e
print("value of x1",x1)
print("value of x2",x2)


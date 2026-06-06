#program to find x^n without pow()
x = int(input("Enter the base(x):"))
n = int(input("Enter the power(n):"))
exp = 1
for i in range (0,n):
    exp = exp * x
print(x,"to the power",n,"=",exp)
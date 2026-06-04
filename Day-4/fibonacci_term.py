#program to find nth term of fibonacci term
n = int(input("enter the term you want to find:"))
print ("The fibonacci term is")
fib = 0
fib1 = 1
if n == 1:
    print(0)
elif n == 2:
    print (1)
else:
    for i in range (3,n+1):
        fib3 = fib + fib1
        fib = fib1 
        fib1 = fib3
    print (fib3)
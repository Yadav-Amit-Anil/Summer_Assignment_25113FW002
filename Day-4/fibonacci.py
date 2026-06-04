#program to generate fibonacci series
num = int(input("Enter the number of terms of fibonacci series:"))
print ("The fibonacci series is:")
fib = 0
fib1 = 1
for i in range (0,num):
    print(fib)
    fib3 = fib + fib1
    fib = fib1
    fib1 = fib3
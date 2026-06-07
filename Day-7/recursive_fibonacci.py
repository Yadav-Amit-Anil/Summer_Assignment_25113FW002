#program for recursive fibonacci
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num = int(input("Enter the term:"))
for i in range (0,num):
    print (fibonacci(i))
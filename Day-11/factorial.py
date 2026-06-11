#program to write function to find factorial
def factorial(a):
    fact = 1
    for i in range (1,a+1):
        fact=fact*i
    return fact
num = int(input("Enter the nuumber:"))
print("factorial:",factorial(num))
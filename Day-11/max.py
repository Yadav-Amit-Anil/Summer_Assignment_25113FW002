#progrm to write function to find maximum
def max(a,b):
    if a>b:
        return a
    else:
        return b
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
print("maximum:",max(num1,num2))
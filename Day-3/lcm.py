# program to find LCM of two numbers
num1 = int( input("Enter the first number:"))
num2 = int( input("Enter the second number:"))
a = num1
b = num2
while (b != 0):
    rem = a % b 
    a = b
    b= rem
    
gcd = a

lcm = (num1 * num2)//gcd
print("LCM:",lcm)
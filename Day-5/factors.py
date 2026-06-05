#program to print factors of a number
num = int(input("Enter the number:"))
print("The factors of",num,"are:")
for i in range (1,num):
    factor = num % i
    if factor == 0:
        print(i)
#program to print prime numbers in a range
num1=int(input("Enter the start of range:"))
num2=int(input("Enter the end of the range:"))
print("The prime numbers are:")
for i in range (num1,num2+1):
    if i > 1:
        for j in range (2,i):
            if i%j == 0:
                break
        else :
            print(i)
           
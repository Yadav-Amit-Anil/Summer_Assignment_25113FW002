#program to write function for perfect number
def perfect(num):
    per = 0
    for i in range (1,num):
        div = num%i
        if div == 0:
            per = per + i
    return num == per
n = int(input("Enter the number you want to check:"))
if perfect(n):
    print("perfect")
else:
    print("not perfect")
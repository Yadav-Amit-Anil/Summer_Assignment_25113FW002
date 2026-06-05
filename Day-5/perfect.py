#program to check perfect number
num = int(input("Enter the number:"))
per = 0
for i in range (1,num):
    div = num%i
    if div == 0:
        per = per + i
if num == per:
    print("The number is perfect.")
else:
    print("The number is not perfect")
#program to check strong number
num = int(input("Enter the number:"))
count = len(str(num))
strong = 0
temp = num
while temp > 0:
    digit = temp % 10
    fact = 1
    for j in range (1,digit+1):
        fact=fact*j
    strong = strong + fact
    temp = temp // 10
if num == strong:
    print("The number is strong.")
else:
    print("The number is not strong.")
#program to write function for armstrong
def armstrong(num):
    count = 0
    temp1 = num
    while temp1 != 0:
        temp1 = temp1 // 10
        count += 1
    arm = 0
    temp2 = num
    for i in range (0,count):
        digit = temp2 % 10
        arm = arm + (digit ** count)
        temp2 = temp2 // 10
    return num == arm
n = int(input("Enter the number you want to check:"))
if armstrong(n):
    print("armstrong")
else:
    print("not armstrong")
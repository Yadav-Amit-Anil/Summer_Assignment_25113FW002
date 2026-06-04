#program to check armstrong number
num = int(input("Enter the number:"))
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
if num == arm :
    print ("It is an armstrong number.")
else:
    print("It is not an armstrong number.")
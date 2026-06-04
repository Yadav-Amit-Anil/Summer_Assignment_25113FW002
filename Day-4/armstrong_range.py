#program to print armstrong numbers in range
start = int ( input("Enter starting number:"))
end = int ( input("Enter the ending number:"))
print("The armstrong numbers between",start,"and",end,"is:")
for num in range (start,end + 1):
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
    if num == arm:
        print(arm)
    
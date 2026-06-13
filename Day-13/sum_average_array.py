#program to find sum and average of array
n = int(input("Enter the number of elemets:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter elements:")))
total = 0
for i in range(n):
    total = total + arr[i]
avg= total/n
print("Sum=",total)
print("Average=",avg)
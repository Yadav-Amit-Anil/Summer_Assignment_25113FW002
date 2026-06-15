#program to reverse an array
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
arr.reverse()
print(arr)
 
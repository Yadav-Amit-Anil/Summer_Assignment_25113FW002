#program to rotate array left
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
d = int(input("Enter number of rotations:"))
d = d % n
arr = arr[d:] + arr[:d]
print("array after left rotation:",arr)
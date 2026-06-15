#program to rotate array right
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
d = int(input("Enter number of rotations:"))
d = d % n
arr = arr[n-d:] + arr[:d+1]
print("array after right rotation:",arr)
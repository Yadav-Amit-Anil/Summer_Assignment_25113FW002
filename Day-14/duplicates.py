#program to find duplicates in array
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
print("Duplicates in array:")
for i in range (n):
    for j in range (1+i,n):
        if arr[i]==arr[j]:
            print(arr[i])
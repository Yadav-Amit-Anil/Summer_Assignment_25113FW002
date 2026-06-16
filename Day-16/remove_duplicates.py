#program to remove duplicates from array
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
i=0
while i<len(arr):
    j = i+1
    while j<len(arr):
        if arr[i]==arr[j]:
            arr.remove(arr[j])
        else:
            j+=1
    i+=1
print("Array after removing duplicates:",arr)
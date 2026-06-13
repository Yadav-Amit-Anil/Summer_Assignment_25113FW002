#program to find largest and smallest element
n = int(input("Enter the number of elemets:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter elements:")))
largest = arr[0]
smallest = arr[0]
for i in range(1,n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]
print("Largest element:",largest)
print("Smallest element:",smallest)
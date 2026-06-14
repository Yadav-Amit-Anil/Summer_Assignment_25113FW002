#program to find second largest element
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
largest = arr[0]
second= arr[0]
for i in range (n):
    if arr[i]>=largest:
        second=largest
        largest=arr[i]
    elif arr[i]>second and largest!=arr[i]:
        second = arr[i]
print("second largest element=",second)
    
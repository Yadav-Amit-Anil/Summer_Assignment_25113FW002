#program to linear search
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
search = int(input("Enter the element you want to search:"))
for i in range (0,5):
    if arr[i]==search:
        print("Element found at index:",i)
        break
else:
    print("Element not found.")
#program to find frequency of an element
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
freq = int(input("Enter the element you want to count:"))
count=0
for i in range (n):
    if freq == arr[i]:
        count+=1
if count==0:
    print("Element not found.")
else:
    print("frequency=",count)
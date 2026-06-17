#program to merge arrays
n1 = int(input("enter the number of elements in array 1:"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("enter element of array 1:")))
n2 = int(input("enter the number of elements in array 2:"))
arr2=[]
for i in range(n2):
    arr2.append(int(input("enter element of array 1:")))
merged=arr1+arr2
print("Merged array=",merged)
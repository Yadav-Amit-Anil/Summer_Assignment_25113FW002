#program to find intersection of arrays
n1 = int(input("enter the number of elements in array 1:"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("enter element of array 1:")))
n2 = int(input("enter the number of elements in array 2:"))
arr2=[]
for i in range(n2):
    arr2.append(int(input("enter element of array 1:")))
intersection = []
for i in range (n1):
    for j in range(n2):
        if arr1[i]==arr2[j]:
            intersection.append(arr1[i])
print("Intersection array=",intersection)
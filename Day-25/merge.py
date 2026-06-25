#program to merge two sorted array
n1 = int(input("Enter number of elements in array 1:"))
arr1 = []
print("Enter the sorted element of arr1")
for i in range (n1):
    arr1.append(int(input(" ")))
n2 = int(input("Enter number of elements in array 1:"))
print("Enter the sorted element of arr2")
arr2 = []
for i in range (n2):
    arr2.append(int(input("")))
merge = []
i=0
j=0
while i<n1 and j<n2:
    if arr1[i]<arr2[j]:
        merge.append(arr1[i])
        i+=1
    else:
        merge.append(arr2[j])
        j+=1
while i<n1:
    merge.append(arr1[i])
    i+=1
while j < n2:
    merge.append(arr2[j])
    j+=1
print("Merged array:",merge)
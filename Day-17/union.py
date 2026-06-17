#program to union of arrays
n1 = int(input("enter the number of elements in array 1:"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("enter element of array 1:")))
n2 = int(input("enter the number of elements in array 2:"))
arr2=[]
for i in range(n2):
    arr2.append(int(input("enter element of array 1:")))
union=arr1+arr2
i=0
while i<len(union):
    j=i+1
    while j<len(union):
        if union[i]==union[j]:
            union.remove(union[j])
        else:
            j+=1
    i+=1
print("Union array=",union)

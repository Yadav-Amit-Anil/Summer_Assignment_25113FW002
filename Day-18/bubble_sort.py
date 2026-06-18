#program to bubble sort
n = int(input("Enter the number of elements:"))
arr=[]
for i in range (n):
    arr.append(int(input("Enter the element:")))
for i in range (n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Sorted array:",arr)
#program for binary search
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
print("Sorted array=",arr)
key =int(input("Enter the element you want to search:"))
small=0
large=n-1
for i in range (small,large+1):
    mid=(small+large)//2
    if arr[mid]==key:
        print("Element found at=",mid)
        break
    elif arr[mid]<key:
        small=mid
    elif arr[mid]>key:
        large=mid

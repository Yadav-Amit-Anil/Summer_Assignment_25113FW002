#program for selection sort
n = int(input("Enter the number of elements:"))
arr=[]
for i in range (n):
    arr.append(int(input("Enter the element:")))
for i in range(n):
    smallest=i
    for j in range (i+1,n):
        if arr[j]<arr[smallest]:
            smallest=j
    temp=arr[i]
    arr[i]=arr[smallest]
    arr[smallest]=temp
print("sorted array:",arr)
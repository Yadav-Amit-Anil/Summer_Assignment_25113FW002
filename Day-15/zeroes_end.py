#program to move zeroes to the end
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter the element:")))
result=[]
count=0
for i in range(n):
    if arr[i]!=0:
        result.append(arr[i])
    else:
        count+=1
for i in range(count):
    result.append(0)
print(result)
#program to find maximum frequency element
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
max_freq=0
element =0
for i in range (n):
    count=0
    for j in range (n):
        if arr[i]==arr[j]:
            count+=1
    if count>=max_freq:
        max_freq=count
        element=arr[i]
print("Maximum frequency=",max_freq)
print("Element=",element)
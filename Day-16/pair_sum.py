#program to find pair with the given sum
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
sum=int(input("Enter the sum of which you want to find sum:"))
for i in range (n):
    for j in range (i+1,n):
        if arr[i]+arr[j]==sum:
            print("Pair found:",arr[i],arr[j])
#program to count even and odd elements
n = int(input("Enter the number of elemets:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter elements:")))
even = 0
odd = 0
for i in range(n):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Number of even elements=",even)
print("Number of odd elements=",odd)
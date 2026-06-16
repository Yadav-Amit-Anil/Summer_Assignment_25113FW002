#program to find missing number from array
n = int(input("Enter the number of elements:"))
arr = []
for i in range (n):
    arr.append(int(input("Enter the element:")))
expected_sum=(n+1)*(n+2)//2
actual_sum =0
for i in range (n):
    actual_sum+=arr[i]
missing_number = expected_sum - actual_sum
print("Missing number=",missing_number)
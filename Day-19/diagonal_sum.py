#program to find diagonal sum
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)
sum=0
for i in range (r):
    for j in range (c):
        if i == j:
            sum = sum + A[i][j]
print("Sum of diagonal:",sum)
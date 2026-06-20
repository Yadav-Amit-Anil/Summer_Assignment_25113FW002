#program to find row-wise sum
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)
print("Row-wise sum:")
for i in range (r):
    s = 0
    for j in range (c):
        s = s + A[i][j]
    print("sum of row",i+1,"=",s)
#program to find column-wise sum
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)
print("column-wise sum:")
for j in range (c):
    s = 0
    for i in range (r):
        s = s + A[i][j]
    print("sum of column",i+1,"=",s)
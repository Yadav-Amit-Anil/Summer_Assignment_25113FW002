#program to add mattices
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)
print("Enter the element of matrix 2:")
B = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)
C = []
for i in range(r):
    row=[]
    for j in range (c):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print("Sum of matrices=")
for i in C:
    print(i)
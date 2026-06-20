#program to check symmetric metrix
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)
B = []
for i in range (c):
    row=[]
    for j in range (r):
        row.append(A[j][i])
    B.append(row)
if A == B:
    print("Mtrix is symmetric.")
else:
    print("Matrix is not symmetric.")
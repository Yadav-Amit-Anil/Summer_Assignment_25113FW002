#program to multiply matrices
r1 = int(input("Enter the number of rows:"))
c1 = int(input("Enter the number of column:"))
print("Enter the element of matrix 1:")
A = []
for i in range (r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)
r2 = int(input("Enter the number of rows:"))
c2 = int(input("Enter the number of column:"))
print("Enter the element of matrix 2:")
B = []
for i in range (r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
if c1 != r1:
    print("Multipliction not possible.")
else:
    C=[]
    for i in range (r1):
        row = []
        for j in range (c2):
            element = 0
            for k in range(c1):
                element=element + (A[i][k]*B[k][j])
            row.append(element)
        C.append(row)
print("Multiplication of matrices:")
for i in C:
    print(i)
#program to print star pyramid
row = 5
for i in range (1,row+1):
    for j in range (1,row+1-i):
         print(" ",end=" ")
    for k in range (1,2*i):
         print("*",end =" ")
    print()
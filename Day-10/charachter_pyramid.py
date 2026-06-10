#program to print charachter pyramid
row = 5
for i in range (row):
    print(" "*(row-i-1),end=" ")
    for j in range (i+1):
         print(chr(65+j),end=" ")
    for j in range (i-1,-1,-1):
         print(chr(65+j),end =" ")
    print()
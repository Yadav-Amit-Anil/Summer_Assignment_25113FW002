#program to print reverse number triangle:
row = 5
for i in range (1,row+1):
    for j in range (1,row+2-i):
        print(j,end=" ")
    print()
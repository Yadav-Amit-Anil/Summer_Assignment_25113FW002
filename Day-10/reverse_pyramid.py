#program to print reverse pyramid
row = 5
for i in range (1,row+1):
    for j in range (1,row+1):
        if j<i:
            print(" ",end=" ")
        else :
            print("*",end=" ")
    for k in range (1,row-i+1):
        print("*",end=" ")
    print()
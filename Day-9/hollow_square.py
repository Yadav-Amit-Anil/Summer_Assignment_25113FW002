#program to print hollow square pattern
row = 5
for i in range (1,row+1):
    for j in range (1,row+1):
        if i==1 or j==1:
            print ("*",end="")
        elif i==5 or j==5:
            print ("*",end="")
        else:
            print(end=" ")
    print()
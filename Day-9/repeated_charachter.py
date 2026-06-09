#program to print repeated charachter pattern
row = 5
for i in range (65,69+1):
    for j in range (1,i-65+2):
        print (chr(i),end=" ")
    print()
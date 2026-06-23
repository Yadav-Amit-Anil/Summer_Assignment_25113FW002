#program to find string length without strlen()
string = str(input("Enter the string:"))
count = 0
for ch in string:
    count+=1
print("length of  string=",count)
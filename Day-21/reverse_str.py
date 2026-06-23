#pprogram to reverse a string
s = str(input("Enter the string:"))
rev = " "
for ch in s:
    rev = ch + rev
print("Reversed string=",rev)
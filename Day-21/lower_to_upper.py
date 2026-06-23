#program to convert lowercase to uppercase
s = str(input("Enter the lowercase string:"))
upper = " "
for ch in s:
    l = ord(ch) - 32
    upper = upper + chr(l)
print("uppercase=",upper)
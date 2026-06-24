#program to remove duplicate charachters
s = input("Enter the string:")
result=""
for ch in s:
    if ch not in result:
        result+=ch
print("Strings after removing duplicates=",result)
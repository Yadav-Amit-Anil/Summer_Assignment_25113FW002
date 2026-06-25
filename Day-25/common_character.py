#program to find common charachters in string
s1 =input("Enter the first string:")
s2 = input("Enter the second string:")
common =""
print("Common charachtes are:")
for ch in s1:
    if ch in s2 and ch not in common:
        common+=ch
        print(ch)
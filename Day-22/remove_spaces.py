#program to remove spaces from string
s = input("Enter the string:")
word = ""
for ch in s:
    if ch != " ":
        word = word + ch
print("String without spaces:",word)
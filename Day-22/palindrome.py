#program to check palindrome string
s = str(input("Enter the string:"))
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("It is palindrome.")
else:
    print("Its not a palindrome.")
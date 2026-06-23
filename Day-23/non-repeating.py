#program to find frst non-repeating charachter
s = input("Enter the string:")
count=0
for ch in s:
    if s.count(ch)==1:
        print("First non-repeating charachter is=",ch)
        break
else:
    print("No non-repeating charachter found.")
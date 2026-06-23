#program to find first repeating charachter
 #program to find frst non-repeating charachter
s = input("Enter the string:")
count=0
for ch in s:
    if s.count(ch)>1:
        print("First repeating charachter=",ch)
        break
else:
    print("No repeating charachters found.")
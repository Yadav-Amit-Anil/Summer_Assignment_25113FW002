#program to find maximum occuring character
s = input("Enter the string:")
char = ""
count = 0
for ch in s:
    if s.count(ch)>count:
        count = s.count(ch)
        char = ch
print("Maximum occuring charachter=",char)
print("Frequency=",count)
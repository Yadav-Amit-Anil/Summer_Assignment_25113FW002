#program to count vowels and consonanats
s = str(input("Enter the string:"))
vow = 0
cons = 0
for ch in s:
    if ch in "AEIOUaeiou":
        vow+=1
    else:
        cons+=1
print("vowels=",vow)
print("Consonants=",cons)
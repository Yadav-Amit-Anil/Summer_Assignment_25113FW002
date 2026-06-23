#program to find character frequency
s = input("Enter the string:")
key = input("Enter the character to find thr frequency:")
count=0
for ch in s:
    if ch == key:
        count+=1
print("Frequency of ",key,"=",count)
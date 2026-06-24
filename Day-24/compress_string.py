#program to compress a string
s = input("Enter the string:")
count=1
comp=""
for i in range(len(s)):
    if i <len(s)-1 and s[i]==s[i+1]:
        count+=1
    else:
        comp += s[i] + str(count)
        count = 1
print("Compressed string=",comp)
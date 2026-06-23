#program to check anagram strings
s1 = input("Enter the first string:")
s2 = input("Enter the second string:")
if sorted(s1) == sorted(s2):
    print("Strings are anagram.")
else:
    print("Strings are not anagram")
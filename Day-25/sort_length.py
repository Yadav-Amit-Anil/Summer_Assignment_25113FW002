#program to sort words by length
n = int(input("Enter number of words:"))
words = []
for i in range(n):
    words.append(input("Enter word:"))
words.sort(key=len)
print("Words sorted by length:")
for i in range(n):
    print(words[i])
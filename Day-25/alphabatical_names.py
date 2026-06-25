#program to sort names alphabatically
n = int(input("Enter the number of names:"))
names = []
for i in range(n):
    print ("Enter name:")
    names.append(input())
names.sort()
print("Sorted names:")
for i in range(n):
    print(names[i])
#program for recursive revrse
def reverse(n):
    if n == 0:
        return str("")
    return str(n%10) + reverse(n//10)
num = int(input("Enter the number:"))
print (reverse(num))
#program for recursive sum of digits
def sum(n):
    if n == 0:
        return 0
    return (n%10) + sum(n//10)
num = int(input("Enter the number:"))
print (sum(num)) 
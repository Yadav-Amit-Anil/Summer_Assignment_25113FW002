#program to write function to check prime
def prime(a):
    if a == 1:
        return False
    else:
        for i in range (2,a):
            rem = a % i
            if rem == 0:
                return False
        return True
num = int(input("Enter the number:"))
print("prime:",prime(num))
            
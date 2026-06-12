#program to write function for palindrome
def palindrome(n):
    temp=n
    reverse = 0
    while n>0:
        digit = n%10
        reverse = reverse * 10 + digit
        n//=10
    return temp == reverse
num = int(input("Enter the number you want to check:"))
if palindrome(num):
    print ("palindrome")
else:
    print("not palindrome")
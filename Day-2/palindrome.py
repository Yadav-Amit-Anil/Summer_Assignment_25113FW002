num = int(input("enter the number:"))
temp=num
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse * 10 + digit
    num//=10
if reverse == temp:
    print("it is a palindrome number.")
else:
    print("it is not a palindrome.")

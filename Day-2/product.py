num = int(input("enter the number:"))
product_of_digits = 1
while num>0 :
    digits = num%10
    product_of_digits *= digits
    num //=10
print("product of digits:",product_of_digits)

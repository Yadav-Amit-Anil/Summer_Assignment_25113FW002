num=int(input("enter the number:"))
sum_of_digits=0
while num>0:
    digit=num%10
    sum_of_digits+=digit
    num=num//10
print("sum of digits:",sum_of_digits)

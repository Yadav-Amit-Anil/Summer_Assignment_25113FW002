#program to find largest prime factor
num = int(input("Enter the number:"))
factor = 1
i=2
while i*i <= num:
    while num % i == 0:
        factor = i 
        num = num //i
    i +=1
if num>1:
    factor = num
print("largest prime factor:",factor)
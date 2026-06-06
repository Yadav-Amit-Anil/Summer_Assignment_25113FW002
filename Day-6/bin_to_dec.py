#progarm to convert binary to decimal
num = int(input("Enter the  number:"))
count = len(str(num))
if num == 0:
    dec = 0
else:
    while num>0:
        dec = 0
        for i in range (0,count):
            rem = num % 10
            dec = dec + (rem * (2 ** i))
            num = num // 10
print ("decimal=",dec)
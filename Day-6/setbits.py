#program to count set bits in a number
num = int ( input( "Enter the number:"))
count = 0
while num > 0:
    rem = num % 2
    if rem == 1:
        count+=1
    num = num//2
print ("Number of set bits =",count)
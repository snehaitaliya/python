import math
n=76543
sum=0

while n>0:
    digit = math.floor(n % 10)
    sum += digit
    n = n / 10

print("The Sum of Digit is :",sum)

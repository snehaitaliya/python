import math
n=5436
r=0

while n>0:
    digit = math.floor(n % 10)
    r= r*10+digit
    n = n / 10

print("The reverse of is :",r)
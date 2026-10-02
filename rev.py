import math
n=int(input("enter N:"))

r=0

while n!=0:
    t=math.floor(n%10)
    r=r*10+t
    n=math.floor(n/10)

print("rev : ",r)
    

import math
n=int(input("Enter N : "))
sum=0
t=n
while n!=0:
    a=math.floor(n%10)
    sum=sum+(a*a*a)
    n=n/10

if t==sum:
    print("Armstrong Number...")
else:
    print("Not Armstrong Number...")

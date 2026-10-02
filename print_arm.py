import math

sum=0
t=0
a=0

while a<=10:
    n=a
    while n!=0:
        t=math.floor(n%10)
        sum=sum+t
        n=math.floor(n/10)

    if sum==a:
        print(sum)
    t=0
    sum=0
    a+=1

    
a=10
while a<=100:
    n=a
    while n!=0:
        t=math.floor(n%10)
        sum=sum+(t*t)
        n=math.floor(n/10)

    if sum==a:
        print(sum)
    t=0
    sum=0
    a+=1


a=100
while a<=1000:
    n=a
    while n!=0:
        t=math.floor(n%10)
        sum=sum+(t*t*t)
        n=math.floor(n/10)

    if sum==a:
        print(sum)
    t=0
    sum=0
    a+=1


a=1000
while a<=10000:
    n=a
    while n!=0:
        t=math.floor(n%10)
        sum=sum+(t*t*t*t)
        n=math.floor(n/10)

    if sum==a:
        print(sum)
    t=0
    sum=0
    a+=1       





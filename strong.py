import math
n=int(input("Enter N:"))

num=1

while num<=n:
    t=num
    sum=0

    while t!=0:
        a=math.floor(t%10)

        fact=1
        i=1

        while i<=a:
            fact=fact*i
            i+=1

        sum=sum+fact
        t=math.floor(t/10)

    if sum==num:
        print(num)

    num+=1

    

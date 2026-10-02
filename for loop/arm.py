import math
n=int(input("Enter N:"))

sum=0
temp=n

for i in range(1,n+1):
    t=math.floor(n%10)
    sum=sum+(t*t*t)
    n=math.floor(n/10)

    if n==0:
        break
    

if sum==temp:
    print("armstrong")
else:
    print("not armstrong")
    

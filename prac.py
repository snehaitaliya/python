n=int(input("enter name : "))
t=n
sum=0
while n!=0:
    r=n%10
    fact=1
    i=1
    while n!=0:
        fact=fact*i
        i+=1
    sum=fact*i
    n=n/10
if sum==t:
    print("strong")
else:
    print("not strong")
    

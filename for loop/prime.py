n=int(input("enter n:"))
cnt=0
for i in range(1,n):
    if n%i==0:
        cnt+=1

if cnt>2:
    print("prime")
else:
    print("not prime")

    

n=int(input("Enter N:"))

num=1

while num<=n:
    i=1
    sum=0

    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1

    if sum==num:
        print(num)
    num+=1
        
    




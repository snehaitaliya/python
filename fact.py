n=int(input("enter N:"))
fact=1
i=1

while i<=n:
    print(i,end="  ")
    if i!=n:
        print("x",end="  ")
    
    fact=fact*i
    i+=1

print("=",fact)


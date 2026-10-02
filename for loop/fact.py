n=int(input("enter n:"))

fact=1
i=1

for i in range(n,0,-1):
    print(i)
    fact=fact*i
    i+=1

print("\nfact = ",fact)

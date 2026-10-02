l=[1,2,1,3,2,1,4,3]

n=len(l)

for i in range(n):
    j=i+1
    while j<n:
        if l[i]==l[j]:
            for s in range(j,n-1):
                l[s]=l[s+1]
            n-=1
        
        j+=1

for i in range(n):
    print(l[i],end="  ")

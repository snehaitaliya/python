t=(2,3,5,6,7,8,1,9,2,5,7)
l=list(t)
n=len(l)
for i in range(n):
    j=i+1
    while j<n:
        if l[i]==l[j]:
            for s in range(j,n-1):
                l[s]=l[s+1]
            n-=1
        
        j+=1

t=tuple(l)
for i in range(n):
    print(t[i],end="  ")

l=[1,3,2,3,1]
j=0
for i in range(len(l)):
    for j in range(j+1,len(l)-1):
        if l[i]==l[j]:
            for s in range(j,len(l)-1):
                l[s]=l[s+1]
            j=j-1

print(l)

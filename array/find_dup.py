l=[34,56,12,78,45,12,34,78]

n=len(l)

for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            print(l[j])

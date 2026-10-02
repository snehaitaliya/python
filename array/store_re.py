'''l=[34,56,12,78,45,12,34,78]
l1=[]
n=len(l)

for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            t=0
            for s in range(len(l1)):
                if l[j]==l1[s]:
                    t=1

            if t==0:
                l1+=[l[j]]

for i in range(n):
    t=0
    for j in range(i):
        if l[i]==l[j]:
            t=1

    if t==1:
        print(l[i],end=" ")'''

l=[34,56,12,78,45,12,34,78]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])



l=[34,56,71,12,97,57]
l1=[]

for i in l:
    if i%2==0:
        l1.append(i)

s=set(l1)
print(s)

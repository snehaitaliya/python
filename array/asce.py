l = [45,67,89,54,24,38,78]


for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t

print("\n",l)

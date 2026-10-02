l=[10,20,30,20,10,40]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])


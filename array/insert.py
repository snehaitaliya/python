l = [89,78,45,25,58,65,94,38]

pos = 3
v = 100
l=l+[0]
for i in range(len(l)-1,pos-1,-1):
    l[i] = l[i-1]
l[pos-1] = v

print(l)

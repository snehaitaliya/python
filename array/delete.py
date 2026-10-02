l = [45,67,89,54,24,38,78]
print(l)
d = 54
j=0
for i in range(len(l)):
    if l[i] == d:
        for j in range(i,len(l)-1):
            l[j]=l[j+1]

for i in range (len(l)-1):
    print("\n",l[i])
    






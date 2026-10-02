l = [45,67,89,54,24,38,78]
n=len(l)

for i in range(n):
    for j in range(n):
        if l[i]<l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t

print("\n",l)

for i in range(n-1):
    if i==n-2:
        print("second large = ",l[i])

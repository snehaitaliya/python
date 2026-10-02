t=(45,67,89,54,24,38,78)
l=list(t)
n=len(l)

l.sort()
print(l)
t=tuple(l)

for i in range(n-1):
    if i==n-2:
        print("second large = ",t[i])


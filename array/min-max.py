l=[12,55,78,54,23,90,43]
max=0
min=l[0]
for i in l:
    if max<=i:
        max=i
    if min>=i:
        min=i
print("max : ",max)
print("min : ",min)

 l=[2,3,5,6,7,8,1,9,2,5,7,9,7,7,7]
s=set(l)
print(l)

for i in s:
    cnt=0
    for j in l:
        if i==j:
            cnt+=1
    print(i," = ",cnt,"time")

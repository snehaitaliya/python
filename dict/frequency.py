l=["apple", "banana", "apple", "pear", "banana", "apple"]
s=set(l)
for i in s:
    cnt=0
    for j in l:
        if i==j:
            cnt+=1
    print(i,"=",cnt,"times")
t=(2,3,5,6,7,8,1,9,2,5,7,9,7,7,7)
print(t)
cnt=0
for i in t:
    temp=0
    for j in t:
        if i==j:
            temp+=1
        if temp>cnt:
            cnt=temp
            f=i
print("Most Frequence Element : ",f)

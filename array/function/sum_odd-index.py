t=(10,20,30,40,50,60)     
print(t)
sum=0
cnt=0     
for i in range(0,len(t)):     
    print("t[%d]= %d"%(cnt,t[i]))    
    cnt=cnt+1
    if i%2==1:
        sum+=t[i]
print("sum = ",sum)

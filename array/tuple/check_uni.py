t=(2,3,5,6,7,8,1,9,2,5,7,9,7,7,7)
n=int(input("Enter Number : "))

cnt=0

for i in t:
   if i==n:
       cnt+=1
if cnt==1:
    print("Unique Number...")
else:
    print("Not Unique Number...")

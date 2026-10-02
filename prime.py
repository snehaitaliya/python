n=int(input("Enter n:"))

i=1
cnt=0

while i<=n:
    if n%i==0:
        print(i)
        cnt+=1       
    i+=1

if cnt<=2:
    print("Prime Number...")
else:
    print("Not Prime Number...")

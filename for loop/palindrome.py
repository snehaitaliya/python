import math
n=int(input("Enter N:"))

rev=0
p=n

for i in range(1,n+1):
    t=math.floor(n%10)
    rev=rev*10+t
    n=math.floor(n/10)

    if n==0:
        break
    

if rev==p:
    print("Palindrome.")
else:
    print("Not Palindrome.")
    

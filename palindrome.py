import math
n=int(input("Enter N : "))
r=0
p=n
while n!=0:
    t=math.floor(n%10)
    r=r*10+t
    n=math.floor(n/10)

if p==r:
    print("palindrome number")
else:
    print("not palindrome number")
    

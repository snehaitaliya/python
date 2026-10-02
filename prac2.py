#find num
"""t=(2,3,4,56,6)
print(t)
n=int(input("n : "))
if n in t:
    print("f")
else:
    print("not")"""

#strong
"""import math
n=int(input("enter n : "))
t=n
sum=0
while n!=0:
    r=math.floor(n%10)
    fact=1
    i=1
    while i<=r:
        fact=fact*i
        i+=1
    sum+=fact
    n=math.floor(n/10)
    

if sum==t:
    print("strong")
else:
    print("not")"""


#print strong
"""import math
n=int(input("enter n : "))
num=1
while num<=n:
    t=num
    sum=0
    
    while t!=0:
        r=math.floor(t%10)
        fact=1
        i=1
        while i<=r:
            fact=fact*i
            i+=1
        sum+=fact
        t=math.floor(t/10)

    if sum==num:
        print(num)
    num+=1"""
    

#armstrong
"""import math
n=int(input("enter n : "))
t=n
sum=0
while n!=0:
    a=math.floor(n%10)
    sum=sum+(a*a*a)
    n=math.floor(n/10)
if sum==t:
    print("arm")
else:
    print("not")"""

#print arm
"""import math
n=int(input("enter n : "))
num=1
while num<=n:
    t=num
    sum=0
    
    while t!=0:
        a=math.floor(t%10)
        sum=sum+(a*a*a)
        t=math.floor(t/10)
    if sum==num:
       print(num)
    num+=1"""

#palindrome
"""import math
n=int(input("enter n : "))
r=0
t=n
while n!=0:
    a=math.floor(n%10)
    r=r*10+a
    n=math.floor(n/10)
if r==t:
    print("pali")
else:
    print("not")"""

#pali print
"""import math
n=int(input("enter n : "))
num=10
while num<=n:
    t=num
    r=0
    while t!=0:
        a=math.floor(t%10)
        r=r*10+a
        t=math.floor(t/10)
    if r==num:
        print(num)
    num+=1"""

#perfect
"""n=int(input("n : "))
t=n
sum=0
else:
    print("not")"""

#print perfect
"""n=int(input("n : "))
num=1
while num<=n:
    t=num
    sum=0
    i=1
    while i<t:
        if t%i==0:
            sum+=i
        i+=1
    if sum==num:
        print(num)
    num+=1"""

#insert
"""l=[56,46,78,10,36]
pos=3
v=100
l=l+[0]
for i in range(len(l)-1,pos-1,-1):
    l[i]=l[i-1]

l[pos-1]=v
print(l)"""

#DELETE
"""l=[34,5,7,67,78,3,45,90]
d=67
n=len(l)
for i in range(n):
    if l[i]==d:
        for j in range(i,n-1):
            l[j]=l[j+1]
for i in range(n-1):
    print(l[i])"""

#merge
"""l1=[34,56,78]
l2=[67,34,10]
l3=[]
l3=l1+l2
print(l3)"""

#secd large
"""l=[45,78,10,35,68]
l.sort()
print(l)
n=len(l)
print("second largest = ",l[n-2])"""

#remove duplicate
"""l=[23,67,10,10,46,34,23,67]
n=len(l)
for i in range(n):
    for j in range(i+1,n-1):
        if l[i]==l[j]:
            for s in range(j,n-1):
                l[s]=l[s+1]
            n-=1
for i in range(n-1):
    print(l[i])"""

#store repeat number
"""l=[34,56,12,78,45,12,34,78]
l1=[]
n=len(l)

for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            t=0
            for s in range(len(l1)):
                if l[j]==l1[s]:
                    t=1
            if t==0:
                l1+=[l[j]]

for i in range(n):
    t=0
    for j in range(i):
        if l[i]==l[j]:
            t=1
    if t==1:
        print(l[i],end=" ")"""

#unique
"""l=[34,56,12,78,45,12,34,78]
print(l)
n=int(input("n : "))
cnt=0
for i in l:
    if i==n:
        cnt+=1
if cnt==1:
    print("unique")
else:
    print("not unique")"""


#sum even
"""l=[3,5,6,7,8,2]
sum=0
for i in l:
    if i%2==0:
        sum+=i
t=tuple(l)
print(sum)"""


#list
"""l = [1, 2, 3, 4, 5]
l1 = []
for i in l:
    #l1.append(i*i)
    #l1.append(i**2)
print(list)"""

'''l = [1, 2, 3, 4, 5]
l1 = [i*i for i in l]
print(l1)'''


#Python map() function
'''l=[1,2,3,4,5]
def get(list):
    return list**2
value=map(get,l)
for i in value:
    print(i) '''


#lambda function
'''l=[1,2,3,4,5]
value=map(lambda list:list**2,l)
print(value)
for i in value:
    print(i)'''

'''l=['gautam','vivek','shailesh']
l1=map(lambda list:list.capitalize(),l)
print(list(l1))'''


#lambda arguments : expression
'''a=lambda a:a+10
print(a(5))'''

'''def x(a):
    return a+10
sum = x(10)
print(sum)'''





    


        


    


    

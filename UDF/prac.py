#square
# def first(n):
#     return n*n
# x=first(5)
# print(x)

#even odd
# def check(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# check(7)

#no arg_no rtn
# def first():
#     print("byy")
# first()

#arg_no rtn
# def first(a):
#     print(a)   
# first(34)

#no arg_rtn
# def first():
#     return 7
# print(first())

#arg_rtn
# def first(a,b):
#     return a+b
# print(first(23,67))

#cube
# def cube(n):
#     print(n*n*n)
# cube(3)

#check pos nagative
# def check(n):
#     if n>=0:
#         print("positive")
#     else:
#         print("nagative")
# check(-65)

#largest
# def find(a,b):
#     print("a:",a,"b:",b)
#     if a>b:
#         print("a is largest")
#     else:
#         print("b is largest")
# find(34,56)

#cnt vowels
# def count(string):
#     cnt=0
#     for i in string:
#         if i in "aeiouAEIOU":
#             cnt+=1
#     return cnt
# x=count("gooood")
# print(x)
#-----------------------------------------------------------------------------
#---> TUPLE

#ascending
# t=(5,6,7,1,4,2,3)
# l=list(t)
# l.sort()
# t=tuple(l)
# print(t)

#ascending
# t=(5,6,7,4,1,2,3)
# l=list(t)

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             t=l[i]
#             l[i]=l[j]
#             l[j]=t
# t=tuple(l)
# print(t)
#------------------------------------------------------------------------------
#reverse
# import math
# n=int(input("Enter N : "))
# t=n
# r=0

# while(n!=0):
#     t=math.floor(n%10)
#     r=r*10+t
#     n=math.floor(n/10)
    
#     if n==0:
#         break
# print(r)

#vowels
# s="tata cuuu"
# v={'a','e','i','o','u','A','O','E','I','U'}
# for i in s:
#     if i not in v:
#         print(i)

#insert
# l=[67,43,98,23,78]
# n=50
# pos=3
# l=l+[0]
# for i in range(len(l)-1,pos-1,-1):
#     l[i]=l[i-1]
# l[pos-1]=n
# print(l)





       



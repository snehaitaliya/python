# import math
# class first:
#     def __init__(self):
#         self.n=int(input(" enter n : "))

#     def logic(self):
#         num=1
#         self.get=[]
#         while num<=self.n:
#             t=num
#             sum=0
#             while t!=0:
#                 r=math.floor(t%10)
#                 fact=1
#                 i=1
#                 while i<=r:
#                     fact=fact*i
#                     i+=1
#                 sum+=fact
#                 t=math.floor(t/10)

#             if sum==num:
#                 self.get+=[num]
#             num+=1

#     def disp(self):
#         for i in self.get:
#             print(i)

# f=first()
# f.logic()
# f.disp()


# import math
# class first:
#     def __init__(self):
#         self.n=int(input("Enter n :"))

#     def logic(self):
#         num=1
#         self.get=[]
#         while num<=self.n:
#             sum=0
#             t=num
            
#             while t>0:
#                 r=math.floor(t%10)
#                 fact=1
#                 i=1

#                 while i<=r:
#                     fact=fact*i
#                     i+=1
#                 sum+=fact
#                 t=math.floor(t/10)
#             if sum==num:
#                 self.get="This number is strong number"
#             else:
#                 self.get="This number is not strong number"
#             num+=1
    
#     def disp(self):
#         print(self.get)


# f=first()
# f.logic()
# f.disp()
        
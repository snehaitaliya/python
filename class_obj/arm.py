# import math
# class first:
#     def __init__(self):
#         self.n=int(input("enter n : "))
    
#     def logic(self):
#         self.num=1
#         self.get=[]
#         while self.num<=self.n:
#             t=self.num
#             sum=0

#             while t!=0:
#                 a=math.floor(t%10)
#                 sum=sum+(a*a*a)
#                 t=math.floor(t/10)

#             if sum==self.num:
#                 self.get+=[self.num]
#             self.num+=1

#     def disp(self):
#         for i in self.get:
#             print(i)

# f=first()
# f.logic()
# f.disp()


import math
class first:
    def __init__(self):
        self.n=int(input("Enter n :"))
        self.num=self.n

    def logic(self):
        x=0
        b=0
        self.get=0
        while self.n>0:
            t=math.floor(self.n%10)
            b+=1
            self.n=math.floor(self.n/10)
        
        self.a=self.num

        while self.num>0:
            d=math.floor(self.num%10)
            x=x+math.pow(d,b)
            self.num=math.floor(self.num/10)

        if x==self.a:
            self.get="This number is armstrong number"
        else:
            self.get="This number is not armstrong number"

    def disp(self):
        print(self.get)

f=first()
f.logic()
f.disp()
            
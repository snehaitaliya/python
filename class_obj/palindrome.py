# import math
# class first:
#     def __init__(self):
#         self.n=int(input("enter n : "))
    
#     def logic(self):
#         num=10
#         self.get=[]
#         while num<=self.n:
#             t=num
#             r=0

#             while t!=0:
#                 a=math.floor(t%10)
#                 r=r*10+a
#                 t=math.floor(t/10)

#             if r==num:
#                 self.get+=[num]
#             num+=1

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
    
    def logic(self):
        num=10
        self.get=[]
        while num<=self.n:
            t=num
            r=0

            while t!=0:
                a=math.floor(t%10)
                r=r*10+a
                t=math.floor(t/10)

            if r==num:
                self.get="This number is palindrome number"
            else:
                self.get="This number is not palindrome number"
            num+=1

    def disp(self):
        print(self.get)

f=first()
f.logic()
f.disp()












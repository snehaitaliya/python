
# class first:
#     def __init__(self):
#         self.n=int(input(" enter n : "))

#     def logic(self):
#         num=1
#         self.get=[]
#         while num<=self.n:
#             t=num
#             sum=0
#             i=1
#             while i<t:
#                 if t%i==0:
#                     sum+=i
#                 i+=1
#             if sum==num:
#                 self.get+=[num]
#             num+=1

#     def disp(self):
#         for i in self.get:
#             print(i)

# f=first()
# f.logic()
# f.disp()


class first:
    def __init__(self):
        self.n=int(input("Enter n :"))

    def logic(self):
        num=1
        self.get=[]
        while num<=self.n:
            t=num
            sum=0
            i=1

            while i<t:
                if t%i==0:
                    sum+=i
                i+=1
            
            if sum==num:
                self.get="This number is perfect number"
            else:
                self.get="This number is not perfect number"
            num+=1

    def disp(self):
        print(self.get)
    
f=first()
f.logic()
f.disp()
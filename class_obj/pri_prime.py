# class first:
#     def __init__(self):
#         self.n=int(input("enter number : "))
    
#     def logic(self):
#         self.get=[]
#         for i in range(1,self.n):
#             cnt=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     cnt+=1
#             if cnt<=2:
#                 self.get+=[i]

#     def disp(self):
#         print(self.get)
    
# f=first()
# f.logic()
# f.disp()



class first:
    def __init__(self):
        self.n=int(input("Enter n :"))

    def logic(self):
        self.get=[]
        for i in range(1,self.n):
            cnt=0
            for j in range(1,self.n):
                if i%j==0:
                    cnt+=1
            if cnt<=2:
                self.get="This number is prime number"
            else:
                self.get="This number is not prime number"
                    
    
    def disp(self):
        print(self.get)

f=first()
f.logic()
f.disp()
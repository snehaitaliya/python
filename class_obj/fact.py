class first:
    def __init__(self):
        self.n=int(input(" enter n : "))

    def logic(self):
        self.fact=1
        self.get=[]
        for i in range(1,self.n+1):
            self.fact*=i
            self.get+=[self.fact]
        self.x=1
    
    def disp(self):
        for i in self.get:
            print("factorial of ",self.x,"=",i)
            self.x+=1

f=first()
f.logic()
f.disp() 
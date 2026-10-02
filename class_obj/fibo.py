class first:
    def __init__(self):
       self.n=int(input("enter number : "))
    
    def logic(self):
        a=0
        b=1
        self.get=[]
        while(a<=self.n):
            self.get+=[a]
            c=a+b
            a=b
            b=c
    def disp(self):
        for i in self.get:
            print(i,end=" ")

        
f=first()
f.logic()
f.disp()
        
    
class first:
    def __init___(self,a,b):
        self.a=a
        self.b=b
        print("A= ",a,"B= ",b)

    def getdata(self):
        print("A= ",self.a,"B= ",self.b)
        c=self.a+self.b
        return c

    def setdata(self):
        print("welcome")



f=first(12,34)

z=f.getdata()
f.setdata()
print("sum= ",z)

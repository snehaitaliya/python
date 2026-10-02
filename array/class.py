class opration:

    def __init__(self,a):
        self.a=a

    def max(self):
        print("max: ",max(self.a))
    def min(self):
        print("min: ",min(self.a))

    def square(self):
        x=[i*i for i in self.a]
        print("square of list:",x)

    def duplicate(self):
        n=len(self.a)
        for i in range(n):
            for j in range(i+1,n):
                if self.a[i]==self.a[j]:
                    print("duplicate number:",self.a[j])

            
x=opration([1,2,3,4,2,1,3])
x.max()
x.min()
x.square()
x.duplicate()

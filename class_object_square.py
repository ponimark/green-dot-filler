class square:
    def getdata(self,n):
        self.num=n
    def calculate(self):
        self.sq=self.num**2
    def display(self):
        print("Square is ",self.sq)

a=eval(input("Enter any number : "))
s=square()
s.getdata(a)
s.calculate()
s.display()

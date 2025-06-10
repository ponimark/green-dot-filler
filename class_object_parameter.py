class square:
    def getdata(self,n):
        self.num=n
    def cal(self):
        self.sq=self.num**2
    def display(self):
        print("Square : ",self.sq)

a=eval(input("Enter number : "))
S=square()
S.getdata(a)
S.cal()
S.display()



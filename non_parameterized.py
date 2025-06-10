class square:
    def __init__(self):
        self.n=int(input("Enter Number :"))
    def cal(self):
        self.sq=self.n**2
    def display(self):
        print("Square : ",self.sq)

S=square()
S.cal()
S.display()



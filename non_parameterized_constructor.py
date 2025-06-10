class square:
    def __init__(self):
        self.n=eval(input("Enter any number : "))
    def calculate(self):
        self.sq=self.n**2
    def display(self):
        print("Square is ",self.sq)

s=square()
s.calculate()
s.display()

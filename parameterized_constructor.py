class square:
    def __init__(self,n1=2):
        self.n=n1
    def calculate(self):
        self.sq=self.n**2
    def display(self):
        print("Square is ",self.sq)

num=eval(input("Enter any number : "))
s=square(num)   # This will run for user defined
s.calculate()
s.display()
s1=square()   # this will run for 2 as n1=2 is default
s1.calculate()
s1.display()
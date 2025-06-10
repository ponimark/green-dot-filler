class Add:
    def getdata(self):
        self.n1=eval(input("Enter first number  :")) #use double underscore for making data private
        self.n2=eval(input("Enter second number :"))

    def sum(self):
        self.a=self.n1+self.n2
    
    def display(self):
        print("Sum is ",self.a)

A=Add()
A.getdata()
A.sum()
A.display()
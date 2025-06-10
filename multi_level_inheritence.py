p=eval(input("Principle Amount : "))
t=eval(input("Time in years : "))
r=eval(input("Rate : "))

class base:
    def amount(self,f):
        self.f=f

class base2:
    def time(self,a):
        self.a=a

class base3:
    def rate(self,b):
        self.b=b
        
class value(base,base2,base3):
    def __init__(self,x,q,z):
        self.amount(x)
        self.time(q)
        self.rate(z)

class calculation(value):
    def cal(self):
        self.SI=(self.f*self.a*self.b)/100 

class answer(calculation):
    def display(self):
        print("SI : %.2f"%self.SI)   

a=answer(p,t,r)
a.cal()
a.display()



class base:
    def length(self,a):
        self.a=a

class base2:
    def width(self,b):
        self.b=b

class derive(base,base2):
    def __init__(self,q,z):  # this variable can be anything
        self.length(q)       # this and below one should be similar for better practice
        self.width(z)

    def cal(self):
        self.area=self.a*self.b


l=eval(input("Enter length : "))
w=eval(input("Enter width : "))
d=derive(l,w)
d.cal()
print("area is %.2f"%d.area)


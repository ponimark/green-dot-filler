p=eval(input("First number : "))
t=eval(input("Second number : "))

class parent:
    def number(self,f,s):
        self.f=f
        self.s=s
    
class child(parent):
    def add(self):
        self.add=self.f + self.s

class child1(parent):
    def sub(self):
        self.sub=self.f - self.s

class display(child,child1):
    def answer(self):
        print("Add : ",self.add)
        print("Sub : ",self.sub)

d=display()
d.number(p,t)
d.add()
d.sub()
d.answer()



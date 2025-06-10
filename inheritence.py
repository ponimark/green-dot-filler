import math
class base:
    def __init__(self,r):
        self.r=r

class derive(base):
    def cal(self):
        self.area=math.pi*self.r*self.r
c=eval(input("Enter radius : "))
d=derive(c)
d.cal()
print("area is %.2f"%d.area)


class Evenodd:
    def getdata(self):
        self.n=int(input("Enter first Number  :"))
    def check(self):
        if self.n%2==0:
            print("even")
        else:
            print("odd")

E=Evenodd()
E.getdata()
E.check()
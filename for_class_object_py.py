class Series:
    def getdata(self):
        self.__n=int(input("Enter number :"))
    def display(self):
        for i in range(1,self.__n+1):
            print(i,end=" ")

S=Series()
S.getdata()
S.display()
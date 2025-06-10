n=int(input("Enter number : "))
n=abs(n)
c=0
while n!=0:
    n=n//10
    c=c+1
print(c)
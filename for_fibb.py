s=int(input("Enter number of terms : "))
a=-1
b=1
for i in range(1,s+1):
    c=a+b
    print(c)
    a=b
    b=c

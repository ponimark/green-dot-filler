n=int(input("Enter number of terms : "))
a=-1
b=1
i=0
while i<n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1
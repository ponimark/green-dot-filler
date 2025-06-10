s=int(input("Enter start number : "))
n=int(input("Enter stop number  : "))
a=str(input("Enter even or odd  :")).lower()
if(n>s):
    match a:
        case "even":
            for i in range(s,n+1):
                if(i%2==0):
                    print(i,end="\n")
        case "odd":
            for i in range(s,n+1):
                if(i%2!=0):
                    print(i,end="\n")
        case _:
            print("Invalid input")
else:
    match a:
        case "even":
            for i in range(s,n-1,-1):
                if(i%2==0):
                    print(i,end="\n")
        case "odd":
            for i in range(s,n-1,-1):
                if(i%2!=0):
                    print(i,end="\n")
        case _:
            print("Invalid input")

p=eval(input("Enter Principal                    : "))
r=eval(input("Enter Rate in percentage per annum : "))
t=eval(input("Enter Time in years                : "))
si=(r*p*t)/100
a=si+p
print("Simple Interest                           : ",si)
print("Amount                                    : ",a)
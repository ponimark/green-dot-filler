n=int(input("Enter number : "))
rev=0
num=n
sum=0
tod=0
while n!=0:
    rev=rev*10+n%10
    sum=sum+n%10
    tod=tod+1
    n=n//10
print(rev)
print("sum ",sum)
print("NOD ",tod)
if(rev==num):
    print("Palindrome")
else:
    print("Not Palindrome") 
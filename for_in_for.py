print("For in For")
for i in range(1,6): #row
    for j in range(1,6): #column
        print(j,end=" ")
    print(end="\n") #if wrote print() then also same default print()=\n   


print("\n\n\nWhile in for")
for i in range(1,6): #row
    j=1
    while(j<6):
        print(j,end=" ")   #printed j so 12345  12345
        j=j+1
    print()


print("\n\n\nFor in While")
i=1
while i<6:
    for j in range(1,6):
        print(i,end=" ")   #printed i in this so 11111 22222 33333
    i=i+1
    print()


print("\n\n\nWhile in While")
i=1
while i<6:
    j=1
    while j<6:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1                    
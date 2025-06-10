def alpha():
    ch=input("Enter any character :")
    if ch.isalpha():
        print("Alphabet")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")
alpha()        
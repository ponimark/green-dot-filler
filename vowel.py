def Vowel():
    ch=input("Enter any character :")
    c=ch.lower()
    if c.isalpha():
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Invalid Input")

Vowel()
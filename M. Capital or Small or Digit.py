x=input()

if x.isalpha():
    print("ALPHA")
    if x.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")

else:
    print("IS DIGIT")
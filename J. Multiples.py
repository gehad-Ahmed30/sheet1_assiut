number=input()

x,y=map(int,number.split())

if x%y==0 or y%x==0:
    print("Multiples")
else:
    print("No Multiples")
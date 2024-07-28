number=input()

a,b,c,d,z=number.split()
a=int(a)
c=int(c)
z=int(z)

if b=='+':
    if a+c==z:
      print('Yes')
    else:
        print(a+c)
elif b=='-':
    if a-c==z:
       print("Yes")
    else:
        print(a-c)
elif b=='*':
    if a*c==z:
       print("Yes")
    else:
        print(a*c)

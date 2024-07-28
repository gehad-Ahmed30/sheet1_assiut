number=input()
a,b,c,d=map(int,number.split())
x=b/b
y=d/b
if (a**x)>(c**y):
    print("YES")
else:
    print("NO")
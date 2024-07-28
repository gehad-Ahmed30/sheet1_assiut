number=input()

if '+' in number:
    x,y=number.split('+')
    x=int(x)
    y=int(y)
    output=x+y
    print(output)
elif '-' in number:
    x,y=number.split('-')
    x=int(x)
    y=int(y)
    output=x-y
    print(output)
elif '/' in number:
    x,y=number.split('/')
    x=int(x)
    y=int(y)
    output=int(x/y)
    print(output)
else:
    x,y=number.split('*')
    x=int(x)
    y=int(y)
    output=x*y
    print(output)


import math

number=input()

x,y=map(int,number.split())

result1=math.floor(x/y)
result2=math.ceil(x/y)
result3=(x+y//2)//y



print(f"floor {x} / {y} = {result1}")
print(f"ceil {x} / {y} = {result2}")
print(f"round {x} / {y} = {result3}")
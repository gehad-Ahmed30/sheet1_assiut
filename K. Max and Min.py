import math
number=input()

x,y,z=map(int,number.split())

maxnum=max(x,y,z)
minnum=min(x,y,z)

print(f"{minnum} {maxnum}")
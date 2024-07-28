number=input()

x,y,z=map(int,number.split())

result=[x,y,z]
results=sorted(result)

for x in results:
    print(x)

print()

for y in result:
    print(y)




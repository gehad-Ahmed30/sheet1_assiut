number=input()
l1,r1,l2,r2=map(int,number.split())

l=max(l1,l2)
r=min(r1,r2)

if l>r:
    print(-1)
else:
    print(f"{l} {r}")


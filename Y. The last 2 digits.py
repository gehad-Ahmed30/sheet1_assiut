number=input()

x,y,z,w=map(int,number.split())

multi=x*y*z*w
multi=(multi%100)

if multi<10:
    print(f"0{multi}")
else:
    print(multi)


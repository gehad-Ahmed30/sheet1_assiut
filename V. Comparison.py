
number = input()

x, s, y = number.split()

x = int(x)
y = int(y)


if s == '>' and x > y:
    print("Right")
elif s == '<' and x < y:
    print("Right")
elif s == '=' and x == y:
    print("Right")
else:
    print("Wrong")





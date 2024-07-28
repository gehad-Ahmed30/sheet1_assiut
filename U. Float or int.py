number=float(input())

number_int=int(number)

if number==number_int:
    print(f"int {number_int}")
else:
    x=number - number_int
    print(f"float {number_int} {x}")
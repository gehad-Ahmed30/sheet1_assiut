number=input()

num1,num2=map(int,number.split())

num1=num1%10
num2=num2%10

print(f"{num1+num2}")
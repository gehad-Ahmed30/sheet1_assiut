number=float(input())

if number>=0 and number<=25:
    print(f"Interval [0,25]")
elif number>25 and number<=50:
    print(f"Interval (25,50]")
elif number>50 and number<=75:
    print(f"Interval (50,75]")
elif number>75 and number<=100:
    print(f"Interval (75,100]")
else:
    print("Out of Intervals")
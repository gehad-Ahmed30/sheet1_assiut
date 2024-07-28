number=int(input())

years=int(number / 365)
reminder_years=number % 365
month=int(reminder_years / 30)
days=reminder_years % 30

print(f"{years} years")
print(f"{month} months")
print(f"{days} days")








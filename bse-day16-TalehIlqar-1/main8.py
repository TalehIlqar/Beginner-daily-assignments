from datetime import date
a = date(1998, 1, 28)
b = date.today()
x = b - a

print(x.days // 365)
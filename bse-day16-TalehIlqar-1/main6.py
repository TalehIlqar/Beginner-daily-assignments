from datetime import date, timedelta, datetime

a = datetime.today()
for i in range(0, 5):
    print(a + timedelta(i))


from datetime import date, timedelta, datetime

datetime_str = '10/10/20'

datetime_object = datetime.strptime(datetime_str, '%d/%m/%y')
y = datetime_object + timedelta(5)

print(y)

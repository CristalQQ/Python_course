from datetime import datetime

my_datetime = datetime(2222, 12, 10, 18, 10, 45)

print(my_datetime.strftime('%d-%b-%Y'))
# разное форматирование даты в веб интерфейсе
print(my_datetime.strftime('%d/%m/%Y %H:%M:%S'))

date_str = '10/12/2222'

converted_date = datetime.strptime(date_str, '%d/%m/%Y')
# конвертация строки в datetime
print(converted_date)


date_time_str = '10/12/2222 12:45:5'

converted_date_time = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M:%S')
print(converted_date_time)

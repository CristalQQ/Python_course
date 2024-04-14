from datetime import datetime

my_datetime = datetime(2222, 12, 10, 18, 10, 45)

print(my_datetime)
print(my_datetime.year)
print(my_datetime.second)
print(my_datetime.microsecond)

print(my_datetime.isoformat())
print(my_datetime.now().microsecond)

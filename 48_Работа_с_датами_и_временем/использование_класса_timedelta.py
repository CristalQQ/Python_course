from datetime import datetime, timedelta

my_datetime = datetime(2222, 12, 10, 18, 10, 45)

print(timedelta)

print(my_datetime + timedelta(days=100, hours=2, minutes=120))
# Добавили с помощью оператора сложение, к заданой дате
print(my_datetime - timedelta(days=100, hours=2, minutes=120))
# Отняли

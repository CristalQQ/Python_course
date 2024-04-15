my_number = 25

if my_number > 0:
    print(my_number, "is positive number")


# Пример if с оператором отрицания not
person_info = {
    'age': 20
}

if not person_info.get('name'):
    # Действия в случаях, если:
    # 1. Ключа 'name' у объекта 'person' нет
    # 2. Ключ 'name' есть, но его значение ложно
    print("Имя отсутствует")

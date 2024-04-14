# 1. Создайте функцию для проверки пароля
# 2. Пароль должен быть минимум 8 символов
# 3. В пароле должно быть:
#   - буквы в нижнем регистре
#   - буквы в верхнем решистре
#   - цифры
#   - специальные символы
# 4. Попросите пользователя ввести пароль в терминале и проверьте его

import re
import string


def check_password(password):
    if len(password) < 8:
        raise TypeError("Пароль должен быть минимум 8 символов")

    if (re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
            re.search(r"[\W_]", password)):
        return "Пароль валидный"
    else:
        return "Пароль невалидный"


while True:
    try:
        user_pussword = input("Введите пароль: ")
        print(check_password(user_pussword))

    except TypeError as e:
        print(e)
    if user_pussword == "exit":
        break

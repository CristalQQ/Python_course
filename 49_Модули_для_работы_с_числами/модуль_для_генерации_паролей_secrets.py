import secrets
import string

all_chars = string.ascii_letters + string.digits + string.punctuation


print(''.join(secrets.choice(all_chars) for i in range(50)))
# Метод choice() выбирает всегда один элемент


# print(string.ascii_letters)
# # Полчучаем последовательность букв в верхнем регистре и нижнем регистре
# print(string.ascii_lowercase)   # Только нижний регистр
# print(string.ascii_uppercase)  # Только верхний регистр
# print(string.digits)    # Только цифры
# print(string.punctuation)  # Только символы

# print(string.ascii_letters + string.digits + string.punctuation)

# С помощью тернарного оператора можно было проверить длину строки,
# если длина строки больше 79 символов, печатаем string is long, иначе
# string is short

string = "Very, very, very, very, very, very, very, very, very, very, very, very, very, long"

print("String is long" if len(string) > 79 else "String is short")

print(len(string))

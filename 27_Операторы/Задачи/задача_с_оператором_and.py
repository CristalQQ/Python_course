# Создайте 2 словаря, у которых одинаковые ключ, значение.
# Используя and, выведите в терминал текст: "словари одинаковые, если 1 словарь равен 2"

one_dict = {'a': 12, 5: True}
two_dict = {'a': 12, 5: True}

one_dict == two_dict and print("Словари одинаковые")
# Если словари одинаковые, то значение выражение будет True
# Словари разные, оператор короткого замыкания вернет значение выражения - False

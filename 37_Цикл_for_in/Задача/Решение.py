# Задача 1:
# 1. Создайте функцию dict_to_list, которая будет конвертировать
# словарь в список кортежей.
# 2. Функция должна принимать словарь, а возвращать списко кортежей,
# в каждом кортеже должен быть пары (key, value) из словаря.
# 3. Если значение ключа - целое число, то его нужно умножить на 2
# перед добавлением в кортеж


def dict_to_list(dict_to_convet):
    list_for_convertion = []
    for k, v in dict_to_convet.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


my_dict = {'a': 124214, 'b': True, 124: 'fewg'}
print(dict_to_list(my_dict))


# Задача 2:
# 1. Создайте функцию filter_list, которая бутдет фильтровать список.
# 2. У функции должно быть два параметра - список и тип значения.
# 3. Функция должна вернуть новый список, в котором оcтанутся только значения
# того типа, который был передан в вызове функции вторым аргументом
# 4. Функцию можно будет вызвать например так:
# filter_list([35, True, 'abc', 10], int) и получить [35, 10]


def filter_list(list_to_filter, value_tupe):
    filtered_list = []
    for elem in list_to_filter:
        if type(elem) == value_tupe:
            filtered_list.append(elem)

        # Not recommended, because bool is subclass of int
            # if isinstance(elem, value_tupe):
            #     filtered_list.append(elem)
    return filtered_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))

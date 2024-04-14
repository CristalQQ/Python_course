# Задача 2:
# 1. Создайте функцию filter_list, которая бутдет фильтровать список.
# 2. У функции должно быть два параметра - список и тип значения.
# 3. Функция должна вернуть новый список, в котором оcтанутся только значения
# того типа, который был передан в вызове функции вторым аргументом
# 4. Функцию можно будет вызвать например так:
# filter_list([35, True, 'abc', 10], int) и получить [35, 10]


def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    # Функция возвращает объект и выполняет итерацию по определенной последовательности
    # Ожидает функцию и последовательность
    return list(filter(check_element_type, list_to_filter))


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))

# 1. Создать список словарей, в нем будет 3 словаря, с помощью распаковки списков
# создайте 3 переменных, каждаая из которых будет содержать один из словарей.
# 2. Создайте функцию, которая будет принимать 2 аргумента, в вызове функции нужно распаковать словарь

my_list_dict = [{'a': 23, 'b': 12}, {'a': 1, 'b': 4}, {'a': True, 'b': 'ok'}]

one_dict, two_dict, three_dict = my_list_dict


def unpacking_dict(a, b):
    return 'ok'


print(unpacking_dict(**one_dict))
print(unpacking_dict(**two_dict))
print(unpacking_dict(**three_dict))

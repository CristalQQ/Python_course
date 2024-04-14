from array import array

my_int_array = array('i', [4, 5, 10, 5, 7, 5])  # 'i' - элементы int

print(my_int_array)
print(type(my_int_array))

my_int_array.append(15)

print(my_int_array)


print(my_int_array.count(5))  # Выводит сколько повторялось значение
my_int_array.pop()  # Удаляет последний элемент из массива

print(my_int_array)
print(len(my_int_array))


for elem in my_int_array:
    print(elem)


print(my_int_array[1])


# Сохранить массив в файле
with open('53_Другие_встроенные_модули/my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

# Создаем пустой массив
imported_array = array('i')  # Элементы int

# Прочтем массив
with open('53_Другие_встроенные_модули/my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()  # Обратная последовательность элементов
print(imported_array)

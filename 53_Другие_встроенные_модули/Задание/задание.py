# Создайте новый файл process_array.py
# В этом файле вы будите ожидать аргументы от пользователя, которые будут являться именем файла из которого необходимо создать массив

import sys
from array import array

filename, name_file_massive, array_elements = sys.argv

new_array = array('i', [int(array_elements)])

dir_file_massive = "53_Другие_встроенные_модули/Задание/" + name_file_massive

with open(dir_file_massive, "wb") as new_file:
    new_array.tofile(new_file)


# Прочтем массив
imported_array = array('i')

with open('53_Другие_встроенные_модули/Задание/new_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 1)
    print(imported_array)

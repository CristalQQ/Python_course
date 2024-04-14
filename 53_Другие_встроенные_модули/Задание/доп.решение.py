import sys
from array import array

name_file_massive = input("Введите название файла массива: ")
user_input = input("Введите элементы массива: ")

dir_file_massive = "53_Другие_встроенные_модули/" + name_file_massive

array_elements = [int(num) for num in user_input.split()]

new_array = array('i', array_elements)

with open(dir_file_massive, "wb") as new_file:
    new_array.tofile(new_file)


# Прочтем массив
# imported_array = array('i')  # Элементы int

# with open('53_Другие_встроенные_модули/new_array.bin', 'rb') as my_file:
#     imported_array.fromfile(my_file, 6)
#     print(imported_array)

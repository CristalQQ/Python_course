class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])

custom_list.print_list_info()   # List has 3 elements

custom_list.append(7)   # Добавляем еще один элемент

custom_list.print_list_info()   # List has 4 elements

print(custom_list.__dict__)
print('')
# print(ExtendedList.__dict__)
print('')
print(object.__subclasses__())

with open('new.txt', 'w') as new_file:  # w - write
    new_file.write("First line in the new file\n")
# Если было содержимое в файле, то оно перезапишется


with open('new.txt', 'a') as new_file:  # a - append
    new_file.write("Second line in the new file\n")
# Строка будет добвалена внизу существующих строк в файле

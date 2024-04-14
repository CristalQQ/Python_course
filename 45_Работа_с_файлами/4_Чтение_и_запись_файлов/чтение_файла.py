with open('test.txt') as test_file:
    print(test_file.read())  # .read() - прочесть все содержимое файла


with open('test.txt') as test_file:
    print(test_file.readlines())
# .readlines() - прочесть все строки файла и поместить их в список

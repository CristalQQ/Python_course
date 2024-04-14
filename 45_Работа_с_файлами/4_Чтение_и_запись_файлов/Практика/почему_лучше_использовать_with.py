test_file = open('test.txt', 'w')

test_file.write("First string\n")
test_file.write("Second string\n")

test_file.close()   # Нельзя прочесть файл после того как мы открыли его в режиме запипси, нужно закрыть и заново открыть

with open('test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
# При использовании инструкции with, после завершения всех операций с файлом, метод .close() вызовится автоматически


test_file = open('test.txt')

print(test_file.read())

test_file.close()   # После каждого открытия или записи файла, его нужно закрыть


with open('test.txt') as test_file:
    print(test_file.read())
# Этот код равносилен предыдущему

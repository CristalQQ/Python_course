# 1. Создайте папку files в текущей папке
# 2. Добавьте два файла first.txt и second.txt в эту папку и запишите в них по 2-3 строки текста
# 3. Прочитайте все строки первого файла
# 4. Прочитайте строки второго файла одна за другой
# 5. Удалите оба файла
# 6. Удалите папку files

from pathlib import Path

files_dir = Path('45_Работа_с_файлами/5_Задача/files')
files_dir.mkdir(exist_ok=True)
# exist_ok - Если такая папку уже есть, то ошибка не будет сгенерирована


first_file = files_dir / 'first.txt'
second_file = files_dir / 'second.txt'


with open(first_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")


with open(second_file, 'a') as f:
    lines = [
        "First line in the second file",
        "Second line in the second file",
        "Last liine in the second file"
    ]
    for line in lines:
        f.write(line + '\n')


with open(first_file) as f:
    print(f.read())


with open(second_file) as f:
    for line in f:
        # OPTION 1
        print(line.strip())

    # # OPTION 2
    # while True:
    #     line = f.readline()
    #     print(line.strip())
    #     # .strip() - убирает пробелы и переходы на новую строку
    #     if not line:
    #         break


if first_file.exists:
    first_file.unlink()

if second_file.exists:
    second_file.unlink()


if files_dir.exists():
    files_dir.rmdir()

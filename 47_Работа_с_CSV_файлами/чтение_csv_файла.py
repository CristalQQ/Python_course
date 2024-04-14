import csv

with open('47_Работа_с_CSV_файлами/test.csv') as csv_file:
    reader = csv.reader(csv_file)
    # Можно добавить  (csv_file, delimiter='') чтобы изменить разделение (по-умолчанию запятая)
    for line in reader:
        print(line)

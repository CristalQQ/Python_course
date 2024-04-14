import csv

with open('47_Работа_с_CSV_файлами/test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    # Можно добавить (csv_file, delimiter=';') чтобы изменить разделение(по-умолчанию запятая)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5235, 'vlad', 1352])
    writer.writerow([442, 'mike', 246])
    writer.writerow([5235, 'alice', 73])

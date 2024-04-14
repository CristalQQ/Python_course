from zipfile import ZipFile
from pathlib import Path

with ZipFile('46_Создание_и_распаковка_zip_архивов/my-files.zip', mode='w') as my_zip_file:
    print(my_zip_file)
    for file in Path('46_Создание_и_распаковка_zip_архивов/my-files').iterdir():
        print(file)
        my_zip_file.write(file)

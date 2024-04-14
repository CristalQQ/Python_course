from zipfile import ZipFile

with ZipFile('46_Создание_и_распаковка_zip_архивов/my-files.zip') as my_zip_file:
    my_zip_file.extractall(
        '46_Создание_и_распаковка_zip_архивов/my-files-unziipped')

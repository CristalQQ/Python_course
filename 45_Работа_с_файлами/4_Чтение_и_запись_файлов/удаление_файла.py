from pathlib import Path

print(Path('new.txt').exists())  # .exists() - Проверяет есть ли такой файл

Path('new.txt').unlink()  # .unlink() - Удаляет файл

print(Path('new.txt').exists())

from pathlib import Path

cwd = Path('/home') / 'cristal' / 'Desktop' / 'Python'

print(cwd.exists())  # exists - проверяет существует ли такой путь

print(Path('.').cwd())

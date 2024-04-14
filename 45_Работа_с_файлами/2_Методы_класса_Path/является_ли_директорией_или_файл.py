from pathlib import Path

print(Path('main.py').is_file())

print(Path('../python').is_file())

print(Path('../Python').is_dir())

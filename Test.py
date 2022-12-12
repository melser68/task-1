from unicodedata import normalize, is_normalized
from pathlib import Path
string_path = 'Нормалізація_файл.txt'
print(is_normalized('NFKD', string_path))


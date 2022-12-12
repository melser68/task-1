from unicodedata import *
string_path = 'Нормалізація_файл.txt'
string_path = normalize('NFKD', string_path)
print(string_path, 'Результат')
print(is_normalized('NFKD', string_path))

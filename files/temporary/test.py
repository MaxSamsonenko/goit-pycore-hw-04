# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# s = b'0123456789'
# small_letters = b'abcdefghijklmnopqrstuvwxyz'
# big_letters = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for i in range(0, len(big_letters)):
#     print 
#     print(f'Byte: {big_letters[i]}')
# print(s[0])  # Виведе: 101 (це ASCII-код символу 'e')

# byte_str = 'some text'.encode()
# print(byte_str)

# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

# for num in [127, 255, 156]:
#   print(hex(num))

# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# print(b'Hello world!'.decode('utf-16'))
# byte_array = bytearray(b'Kill Bill')
# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array)

# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'

# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")

from pathlib import Path
import shutil

# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 

# relative_path = Path("example.txt")
# absolute_path = relative_path.absolute()
# print(absolute_path)

# Початковий шлях до файлу
# original_path = Path("example.txt")

# # Зміна імені файлу
# new_path = original_path.with_name("report.txt")
# print(new_path)

# original_path = Path("files/example.txt")

# # Зміна імені файлу
# new_path = original_path.with_suffix(".md")
# print(new_path)

# original_path = Path("files/report.txt")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("example.csv")
# original_path.rename(new_path)

# Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")

# file_path = Path("example.txt")

# # Читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)

# Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Бінарні дані для запису
# data = b"Python is great!"

# # Запис байтів у файл
# file_path.write_bytes(data)

# Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Читання байтів з файлу
# binary_data = file_path.read_bytes()
# print(binary_data)

# Створення об'єкту Path для директорії
# directory = Path("./files")

# # Виведення переліку всіх файлів та піддиректорій
# for path in directory.iterdir():
#     print(path)

# directory = Path('./files/new_folder')
# # directory.mkdir(parents=True, exist_ok=True)
# directory.rmdir()




# # Вихідний і цільовий файли
# source = Path('files/example.csv')
# destination = Path('test_folder/example.csv')

# # Копіювання файла
# shutil.copy(source, destination)

# Вихідний і цільовий шляхи
# source = Path('files/example.bin')
# destination = Path('test_folder/example.bin')

# # Переміщення файла
# shutil.move(source, destination)

from colorama import Fore, Back, Style

print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст на зеленому фоні')
print(Style.RESET_ALL)
print('Це звичайний текст після скидання стилю')
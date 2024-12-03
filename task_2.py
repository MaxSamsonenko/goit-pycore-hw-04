def get_cats_info(path):
    cats = []
    with open(path, 'r', encoding='utf-8') as file:
        lines = [el.strip() for el in file.readlines()]
        for line in lines:
            id, name, age = line.split(',')
            cats.append({"id": id, "name": name, "age": age})
        
    return cats
        
try:
    cats_info = get_cats_info("files/cats_file.txt")
    print(cats_info)
except FileNotFoundError:
    print("Файл не знайдено. Перевірте шлях до файлу.")
except ValueError as e:
    print(f"Помилка у форматі файлу: {e}")
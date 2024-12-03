
def total_salary(path):
    total = 0
    average = 0
    with open(path, 'r', encoding='utf-8') as file:
        lines = [el.strip() for el in file.readlines()]
        for line in lines:
            name, salary = line.split(',')
            total += float(salary)
    average = total / float(len(lines))
    return total, average


try:
    total, average = total_salary("files/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError:
    print("Файл не знайдено. Перевірте шлях до файлу.")
except ValueError as e:
    print(f"Помилка у форматі файлу: {e}")

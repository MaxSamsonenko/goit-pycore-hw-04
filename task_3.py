import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def structure_directory(directory_path):
    try:
        path = Path(directory_path)
        
        if not path.exists():
            print(Fore.RED + "Помилка: Вказаний шлях не існує.")
            return
        if not path.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не є директорією.")
            return

        print(Fore.GREEN + f"Структура директорії: {directory_path}")

        def search_directory(current_path, indent=0):
            for item in current_path.iterdir():
                if item.is_dir():
                    print("  " * indent + Fore.BLUE + f"[{item.name}]")
                    search_directory(item, indent + 1)
                elif item.is_file():
                    print("  " * indent + Fore.YELLOW + item.name)

        search_directory(path)
    
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python hw03.py /шлях/до/вашої/директорії")
    else:
        directory_path = sys.argv[1]
        structure_directory(directory_path)

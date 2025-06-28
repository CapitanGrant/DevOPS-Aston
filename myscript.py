import random
from pathlib import Path
from time import sleep

lst = ['aston', 'task', '3', 'lesson', 'course', 'git', 'python']

new_dir = Path("C:/Users/roman/aston/opt/app")
new_dir.mkdir(parents=True, exist_ok=True)


def random_string():
    string = " + ".join(random.choices(lst, k=3))
    return string


print(f"Директория создана: {new_dir}")

log_file = new_dir / "log.txt"


def log_write(string):
    with open(log_file, "a") as f:
        f.write(string + "\n")


def log_read():
    with open(log_file, "r") as f:
        file = f.read()
        print("Содержимое файла:")
        print(file)


while True:
    string = random_string()
    print(f"Сгенерированная строка: {string}")
    log_write(string)
    log_read()
    sleep(17)

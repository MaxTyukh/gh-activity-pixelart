import os
import subprocess
import argparse
from datetime import datetime, timedelta

COMMITS_PER_PIXEL = 3

def make_commit(date, index):
    # Додаємо секунди, щоб коміти були унікальними
    commit_date = date.replace(hour=12, minute=index % 60, second=index % 60).isoformat()
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_date
    env["GIT_COMMITTER_DATE"] = commit_date
    
    cmd = [
        "git", "commit", "--allow-empty", 
        "-m", f"Art commit {index}", 
        "--date", commit_date
    ]
    
    subprocess.run(cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def main():
    parser = argparse.ArgumentParser(description="GitHub Contribution Art Tool")
    parser.add_argument("--start", type=str, required=True, help="Дата першої неділі у форматі YYYY-MM-DD")
    parser.add_argument("--file", type=str, default="data.txt", help="Шлях до файлу з пікселями")

    args = parser.parse_args()

    try:
        start_date = datetime.strptime(args.start, "%Y-%m-%d")
        if start_date.weekday() != 6:
            print(f"Увага: Дата {args.start} не є неділею. Малюнок може зміститися по вертикалі!")
    except ValueError:
        print("Помилка: Неправильний формат дати. Використовуй YYYY-MM-DD")
        return

    if not os.path.exists(args.file):
        print(f"Помилка: Файл {args.file} не знайдено!")
        return

    print(f"Малюємо, починаючи з {args.start}...")

    with open(args.file, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
                
            pairs = line.split(";")
            for pair in pairs:
                try:
                    coords = pair.strip().split(",")
                    if len(coords) != 2: continue
                    x, y = map(int, coords)
                    target_date = start_date + timedelta(weeks=x, days=y)
                    
                    # {COMMITS_PER_PIXEL} комітів для максимальної яскравості
                    for i in range(COMMITS_PER_PIXEL):
                        make_commit(target_date, i)
                except ValueError:
                    continue

    print("\nГотово! Тепер виконай: git push origin main")

if __name__ == "__main__":
    main()

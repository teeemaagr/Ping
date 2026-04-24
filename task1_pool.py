import time
import random
from concurrent.futures import ThreadPoolExecutor


def task(i):
    sleep_time = random.randint(1, 3)
    print(f"Задача {i} спит {sleep_time} сек")
    time.sleep(sleep_time)
    print(f"Задача {i} завершена")


if __name__ == "__main__":
    print("СТАРТ")

    start = time.time()

    for i in range(5):
        task(i)

    end = time.time()
    print("\nПоследовательно:", round(end - start, 2), "сек")

    start = time.time()

    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(5):
            executor.submit(task, i)

    end = time.time()
    print("Параллельно:", round(end - start, 2), "сек")
import threading
import time


class ThreadSafeDatabase:
    def __init__(self):
        self.data = []
        self.lock = threading.Lock()

    def write(self, value):
        with self.lock:
            print(f"[WRITE] добавляем {value}")
            self.data.append(value)
            time.sleep(1)

    def read(self):
        with self.lock:
            print(f"[READ] данные: {self.data}")
            time.sleep(0.5)


db = ThreadSafeDatabase()


def reader():
    while True:
        db.read()


def writer():
    i = 0
    while True:
        db.write(i)
        i += 1

for _ in range(5):
    threading.Thread(target=reader, daemon=True).start()

for _ in range(2):
    threading.Thread(target=writer, daemon=True).start()

time.sleep(10)
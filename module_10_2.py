import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов

    def run(self):
        print(f"{self.name}, на нас напали!")

        days = 0  # Количество дней сражения

        while self.enemies > 0:
            time.sleep(1)  # 1 секунда = 1 день сражения
            days += 1
            self.enemies -= self.power

            if self.enemies < 0:  # Если врагов стало меньше 0, установить к 0
                self.enemies = 0

            print(f"{self.name} сражается {days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(я)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения битвы
first_knight.join()
second_knight.join()

# Вывод надписи об окончании битвы
print("Сражения окончены.")
class PerformanceLogger:                                   # Класс-декоратор
    def __init__(self, func):                              # Сохраняем оборачиваемую функцию
        self.func = func

    def __call__(self, *args, **kwargs):                   # Делает объект вызываемым
        import time                                        # Импорт внутри метода
        start = time.perf_counter()                        # Засекаем начало

        result = self.func(*args, **kwargs)                # Выполняем функцию

        end = time.perf_counter()                          # Засекаем конец
        print(f"Функция '{self.func.__name__}' завершена за {end - start:.6f} секунд")

        return result                                      # Возвращаем результат


@PerformanceLogger                                         # Применяем декоратор
def factorial(n):                                          # Вычисление факториала
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@PerformanceLogger                                         # Применяем декоратор
def random_string(length=10):                              # Генерация случайной строки
    import random
    import string
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == '__main__':                                 # Точка входа
    print("Вычисление факториала:")
    print("Результат:", factorial(5))
    print()

    print("Генерация случайной строки:")
    print("Результат:", random_string(12))
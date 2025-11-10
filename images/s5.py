class InvalidInputError(Exception):                         # Собственное исключение
    pass


def check_positive(number):                                # Проверяет, что число положительное
    if number <= 0:
        raise InvalidInputError(f"Число {number} не является положительным.")
    print(f"Число {number} корректно: оно положительное.")


def check_non_empty_string(text):                          # Проверяет, что строка не пустая
    if not text.strip():
        raise InvalidInputError("Строка пустая")
    print(f"Строка '{text}' корректна: она не пустая")


if __name__ == '__main__':                                 # Точка входа в программу
    print("Проверка положительного числа:")
    try:
        check_positive(5)                                  # Корректный вызов
    except InvalidInputError as e:
        print(e)

    try:
        check_positive(-3)                                 # Некорректный вызов
    except InvalidInputError as e:
        print(e)

    print("\nПроверка непустой строки:")
    try:
        check_non_empty_string("Hello")                    # Корректный вызов
    except InvalidInputError as e:
        print(e)

    try:
        check_non_empty_string("   ")                      # Некорректный вызов
    except InvalidInputError as e:
        print(e)
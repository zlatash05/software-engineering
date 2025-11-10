def add_two(user_input):
    try:
        number = float(user_input)
        result = 2 + number
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных.Ожидается число.")


print("Тест1:Ввод числа")
add_two("5")

print("\nТест2:Ввод числа дробного")
add_two("3.14")

print("\nТест3:Ввод строки")
add_two("hello")

def add_expense(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        expense = input("Введите описание расхода и сумму: ")
        file.write(expense + "\n")
    print("Расход добавлен!")

def show_expenses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            expenses = file.readlines()
            if expenses:
                print("\nВаши расходы:")
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}. {expense.strip()}")
            else:
                print("Расходов нет.")
    except FileNotFoundError:
        print("Файл с расходами не найден.")

add_expense("expenses.txt")
add_expense("expenses.txt")
add_expense("expenses.txt")
show_expenses("expenses.txt")
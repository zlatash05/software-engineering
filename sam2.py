import random

def roll_dice():
    number = random.randint(1, 6)
    print(f"Выпало: {number}")

    if number == 5 or number == 6:
        print("Вы победили")
    elif number == 3 or number == 4:
        roll_dice()  # Исправлено
    elif number == 1 or number == 2:
        print("Вы проиграли")

if __name__ == "__main__":
    roll_dice()


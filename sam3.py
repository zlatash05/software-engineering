
with open('input3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines = text.split('\n')
num_lines = len(lines)

words = text.split()
num_words = len(words)

num_letters = 0
for char in text:
    if char.isalpha() and char.isascii():
        num_letters += 1

print(f"Количество букв латинского алфавита: {num_letters}")
print(f"Количество слов: {num_words}")
print(f"Количество строк: {num_lines}")



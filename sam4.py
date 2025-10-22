
with open('input4.txt', 'r', encoding='utf-8') as file:
    banned_words = file.read().split()

text = input("Введите предложение: ")

result = text

for word in banned_words:
    start = 0
    while True:
        pos = result.lower().find(word.lower(), start)
        if pos == -1:
            break

        stars = '*' * len(result[pos:pos + len(word)])
        result = result[:pos] + stars + result[pos + len(word):]
        start = pos + len(stars)

print("Результат:", result)

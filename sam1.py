from collections import Counter
import string

with open('input2.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

print(f"Количество слов: {len(words)}")

word_count = Counter(words)
most_common_word, count = word_count.most_common(1)[0]

print(f"Самое частое слово: '{most_common_word}'")
print(f"Количество вхождений: {count}")





def analyze(s):
    print(f"\nПредложение: '{s}'")
    print(f"Длина: {len(s)}")
    print(f"В нижнем регистре: {s.lower()}")

    vowels = sum(1 for char in s.lower() if char in 'aeiou')
    print(f"Гласных: {vowels}")

    replaced = s.replace('ugly', 'beauty').replace('Ugly', 'Beauty')
    print(f"После замены ugly на beauty: '{replaced}'")

    print(f"Начинается с 'The': {s.startswith('The')}")
    print(f"Заканчивается на 'end': {s.endswith('end')}")

sentences = [
    "The weather is bad",
    "I am ugly",
    "This is the end"
]

for sentence in sentences:
    analyze(sentence)



with open('input5.txt', 'r', encoding='utf-8') as file:
    text = file.read()

upper_text = text.upper()


with open('input5.txt', 'w', encoding='utf-8') as file:
    file.write(upper_text)


print("верхний регистр:")
print(upper_text)
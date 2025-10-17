from collections import Counter
def top_3_digits(digits):
    counts = Counter(int(d) for d in digits)
    top_3 = dict(counts.most_common(3))

    sorted_top_3 = dict(sorted(top_3.items()))
    return sorted_top_3

digits = "123456789061236451234656123"
result = top_3_digits(digits)

for key, value in result.items():
    print(f"Число {key}: {value} раз(а)")

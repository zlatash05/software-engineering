from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

a, b, c = min(one), min(two), min(three)
p = (a + b + c) / 2
min_square = sqrt(p * (p - a) * (p - b) * (p - c))


a, b, c = max(one), max(two), max(three)
p = (a + b + c) / 2
max_square = sqrt(p * (p - a) * (p - b) * (p - c))

print ("Минимальная площадь: ", min_square)
print ("Максимальная площадь: ", max_square)
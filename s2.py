def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open("fib.txt", "w", encoding="utf-8") as f:
    for num in fib(200):
        f.write(str(num) + "\n")

with open("fib.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines[-1].strip())
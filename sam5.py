list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

for list in [list_1, list_2, list_3]:
    result = set()

    for num in set(list):
        count = list.count(num)

        for i in range(1, count + 1):
            if i == 1:
                result.add(num)
            else:
                result.add(str(num) * i)

    print(result)
    
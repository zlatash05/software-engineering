def extract_section(tup, element):
    try:
        first_index = tup.index(element)
    except ValueError:
        return ()

    try:
        second_index = tup.index(element, first_index + 1)
        return tup[first_index : second_index + 1]
    except ValueError:
        return tup[first_index:]

my_tuple = (6, 1, 3, 2, 5)
element = 2

result = extract_section(my_tuple, element)
print("Результат:", result)

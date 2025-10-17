def remove_all(tup, value):

    new_tup = tuple(x for x in tup if x != value)
    return new_tup

print(remove_all((2, 1, 3, 5, 6, 2), 2))





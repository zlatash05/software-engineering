def update_shopping_list(items, remove_item, add_item):

    items = list(items)
    if remove_item in items:
        items.remove(remove_item)
    items.append(add_item)
    return tuple(items)

print(update_shopping_list(("хлеб", "молоко", "яйца"), "молоко", "сок"))
print(update_shopping_list(("хлеб", "молоко", "яйца"), "сыр", "фрукты"))
print(update_shopping_list(("картошка", "морковь", "лук"), "лук", "лук"))
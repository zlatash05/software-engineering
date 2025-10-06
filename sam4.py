first = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
second = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

first_new_list = [4 if x == 3 else x for x in first if x != 2]
second_new_list = [4 if x == 3 else x for x in second if x != 2]
three_new_list = [4 if x == 3 else x for x in three if x != 2]

print ("Первый новый список: " , first_new_list)
print ("Второй новый список: " , second_new_list)
print ("Третий новый список: "  , three_new_list)


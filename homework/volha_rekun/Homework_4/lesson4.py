# Задание
# Создание словаря

# 1. Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.

# my_dict = {}
my_dict = {'tuple1': '', 'list1': '', 'dict1': '', 'set1': ''}

# 2. Для каждого элемента задайте значение соответствующее названию ключа.
# Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения.
my_dict['tuple1'] = (5, 4, 3, 2, 1)

my_dict['list1'] = [56, 99, 'hilist', 9, 'no']

my_dict['dict1'] = {'zero': 2, 'one': 5, 'two': 9, 'three': 999, 'four': 3}

my_dict['set1'] = {4, 6, 2, 7, 1}

# Содержимое этого кортежа (или что вы там добавляете) - количество элементов в каждом таком значении
#  должно быть не меньше пяти. Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5),
# если список, то не меньше пяти элементов, если словарь, то не меньше пяти пар ключ-значение, итд.

# 3. Действия с элементами словаря my_dict:

# 4. Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
# print(my_dict['tuple1'[-1]])

last_elem = my_dict['tuple1'][-1]
print("Last element:", last_elem)

# 5. Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент
# my_dict ['list1'] = 'list1.append('new')

add_new = my_dict['list1'].append('new_el_w_konec_spiska')

# 6. удалите второй элемент списка

remove_el = my_dict['list1'].pop(1)

# 7. Для того, что хранится под ключом ‘dict’:добавьте элемент с ключом ('i am a tuple',) и любым значением

my_dict['dict1'][('i am a tuple', )] = 'tuple, tuple, tule'

# 8. удалите какой-нибудь элемент

del my_dict['dict1']['one']

# 9. Для того, что хранится под ключом ‘set’:добавьте новый элемент в множество
add_new_set_el = my_dict['set1'].add('another_one_el')

# 10. удалите элемент из множества
remove_set_el = my_dict['set1'].pop()

# print(my_dict)

# 11. В конце выведите на экран весь словарь

print(my_dict.items())

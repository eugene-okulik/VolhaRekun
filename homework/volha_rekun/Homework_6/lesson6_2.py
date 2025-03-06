# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
# Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
# Вывод должен быть следующим: 1 2 fuzz 4 buzz fuzz 7 8 .. 14 FuzzBuzz 16 ...
# Подсказка: При тестировании своей программы обращайте внимание на числа 3, 5 и 15
# (точнее на то, что должно быть напечатано вместо них)
# Последовательность от 1 до 100 можно создать с помощью range(1, 101)

numbers = list(range(1, 101))
updated_numbers_list = []

for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        updated_numbers_list.append("FuzzBuzz")
    elif number % 5 == 0:
        updated_numbers_list.append("Buzz")
    elif number % 3 == 0:
        updated_numbers_list.append("Fuzz")
    else:
        updated_numbers_list.append(number)

for updated_number in updated_numbers_list:
    print(updated_number)

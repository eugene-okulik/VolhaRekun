import sys

# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

sys.set_int_max_str_digits(1000000)


def fibonnachi():
    # 0, 1, 1, 2, 3, 5, 8, 13
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonnachi()
for n in range(4):
    next(gen)
print("Пятое число:", next(gen))
for n in range(200 - 6):
    next(gen)
print("Двухсотое число:", next(gen))
for n in range(1000 - 201):
    next(gen)
print("Тысячное число:", next(gen))
for n in range(100000 - 1001):
    next(gen)
print("Стотысячное число:", next(gen))

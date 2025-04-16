# Задание №1
# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished"после выполнения декорированной функции.
# Код, использующий этот декоратор может выглядеть, например, так:

# @finish_me
# def example(text):
#     print(text)

# example('print me')
# В результате работы будет такое:

# print me

# finished

def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # вызываем исходную функцию
        print("finished")
        return result
    return wrapper


@finish_me
def example(text):
    print("print me")


example("print me")

# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция

# Код, использующий этот декоратор может выглядеть, например, так:

# @repeat_me
# def example(text):
#     print(text)

# example('print me', count=2)
# В результате работы будет такое:

# print me

# print me


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        result = None
        for _ in range(count):
            result = func(*args, **kwargs)  # вызываем исходную функцию
            print()
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me", count=2)


# Задание №3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)

# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def calc_me(func):
    def wrapper(*args, **kwargs):
        result = None
        a = int(input("vvedite 1 czislo: "))
        b = int(input("vvedite 2 czislo: "))

        if a == b:
            func(a, b, '+')
        elif a > b:
            func(b, a, '-')
        elif b > a:
            func(a, b, '/')
        elif a < 0 or b < 0:
            func(a, b, '*')

        return result
    return wrapper


@calc_me
def calc(first=0, second=0, operation="+"):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    elif operation == '*':
        print(first * second)


calc()


# List comprehension
# Дан такой кусок прайс листа:

# (Копируйте эту переменную (константу) в код прямо как есть)

# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:

# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.

# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_dict = {
    line.split(" ")[0]: int(line.split()[1][:-1])
    for line in PRICE_LIST.splitlines()
}
print(new_dict)

import random

# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.

# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

# Примеры результатов:

# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

# salary = int
# bonus = bool

salary_input = int(input('Введите salary:'))

bonus = random.choice([True, False])

original_salary = salary_input

if bonus:
    random_bonus = random.randint(1,10000)
    salary_input = salary_input + random_bonus

print(f"{original_salary}, {bonus} - '${salary_input}'")

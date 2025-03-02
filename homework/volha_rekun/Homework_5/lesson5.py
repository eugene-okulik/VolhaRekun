# Задание 1
# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат операции: 514
# результат работы программы: 9
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

stroka1 = 'результат операции: 42'
stroka2 = 'результат операции: 514'
stroka3 = 'результат работы программы: 9'

# print(stroka1.index((':')))
print(int((stroka1[stroka1.index(':') + 1:].strip())) + 10)
print(int((stroka2[stroka2.index(':') + 1:].strip())) + 10)
print(int((stroka3[stroka3.index(':') + 1:].strip())) + 10)

# Задание 3
# Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
my_new_string = f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}'
print(my_new_string)

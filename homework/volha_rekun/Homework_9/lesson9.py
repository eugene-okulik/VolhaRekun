# Обработка даты

# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты (January)
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"


import datetime


time_from_task = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(time_from_task, '%b %d, %Y - %H:%M:%S')

print("дата из задачи: ", time_from_task)
print("дата в питоновском формате: ", python_date)

month_name = python_date.strftime('%B')
print("название месяца:", month_name)

human_date = python_date.strftime('%d.%m.%Y, %H:%M')
print("человеческий формат: ", human_date)

# Map, filter
# Есть такой список:

# temperatures =
# [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29,
#  31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

list_of_temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23,
                        25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

list_of_hot_temperatures = []


def hot_temp(x):
    return x > 28


list_of_hot_temperatures = list(filter(hot_temp, list_of_temperatures))
print("список с жаркими днями: ", list(list_of_hot_temperatures))
print("макс темп: ", max(list_of_hot_temperatures))
print("мин темп: ", min(list_of_hot_temperatures))

average_temp = sum(list_of_hot_temperatures) / len(list_of_hot_temperatures)
print("средн темп: ", average_temp)

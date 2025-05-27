import os
from datetime import datetime, timedelta
import re

# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
# Файлик не копируйте и никуда не переносите.
# Напишите программу, которая читает этот файл,
# находит в нём даты и делает с этими датами то, что после них написано

# Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер,
# потом дата,
# потом дефис и
# текст
# У вас должен получиться код, который находит даты и для даты под номером один.
# В коде должно быть реализовано то действие, которое написано в файле после этой даты. Ну и так далее для каждой даты.

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
print(file_path)
homework_path = os.path.dirname(os.path.dirname(base_path))  # путь до папки Homework
teacher_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(teacher_file_path)

# with open(teacher_file_path) as teacher_file:
#     print(teacher_file.read())

# что почитали в файлике:
# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже. Должн получиться 2023-12-04 20:34:13.212967
# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата


with open(teacher_file_path, encoding='utf8') as file:
    for index, line in enumerate(file):
        # print(index)
        match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+", line)
        if match:
            if index == 0:
                # нашли дату в этой строке
                date_str = match.group()
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
                new_date = date_obj + timedelta(weeks=1)
                print('нашли первую дату:', date_obj)
                print('изменили первую дату:', new_date)
            if index == 1:
                date_str = match.group()
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
                day_of_the_week = date_obj.strftime('%A')
                print('нашли вторую дату:', date_obj)
                print('вторая дата- это какой день недели?', day_of_the_week)
            if index == 2:
                date_str = match.group()
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
                now = datetime.now()
                how_many_days_before = (now - date_obj)
                print('нашли третью дату:', date_obj)
                print('сколько дней назад была эта дата?', how_many_days_before)

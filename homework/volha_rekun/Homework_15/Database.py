# Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.

# То есть, в этом задании вы создаете программу, которая
# добавляет студента, +
# добавляет группу, +
# определяет добавленного студента в только что созданную группу, +
# создает в базе книги  и +
# укажите, что ваш созданный студент взял их+
# Создайте несколько учебных предметов (subjects)+
# Создайте по два занятия для каждого предмета (lessons)+
# Поставьте своему студенту оценки (marks) для всех созданных вами занятий+

# Важно: никакие id не хардкодить! Хардкод - это если вы в коде пишете значение id.
# Все id нужно сохранять в переменные сразу после добавления данных в базу и потом ими пользоваться.
# При получении данных, распечатывайте эти данные.


# %%
# Импорт и подключение к базе
import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl'
)

# %%
# INSERT нового студента
# создаем студента точнее добавляем
cursor = db.cursor()
query = "INSERT INTO students(name, second_name) VALUES (%s, %s)"
values = ('Volha4', 'Rekun4')
cursor.execute(query, values)
student_id = cursor.lastrowid
db.commit()
print("добавленный студент:", student_id)


# %%
# INSERT новой группы
# добавляем группу и отображаем
cursor = db.cursor()
query = "INSERT INTO `groups`(title, start_date , end_date) VALUES (%s, %s,%s)"
values = ('AQA_2025_summer3', '06_2025', '09_2025')
cursor.execute(query, values)
group_id = cursor.lastrowid
db.commit()
print("добавленная группа:", group_id)

# %%
# SELECT добавленной группы со всеми данными
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
print("данные о добавленной группе:", cursor.fetchall())


# %%
# UPDATE студента в новую группу
query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)
db.commit()


# %%
# SELECT cтудента по новоопределенной группе
cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
print(cursor.fetchall())


# %%
# INSERT новой книги и указание что студент ее взял
cursor = db.cursor()
query = "INSERT INTO books(title, taken_by_student_id) VALUES (%s, %s)"
values = ('PHP for beginners', student_id)
cursor.execute(query, values)
book_id = cursor.lastrowid
db.commit()
print("добавленная книга:", book_id)

# %%
# SELECT созданной добавленной книги
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())


# %%
# INSERT нового учебного предмета
cursor = db.cursor()
query = "INSERT INTO subjets(title) VALUES (%s)"
cursor.execute(query, ('Polish v3',))
subject1_id = cursor.lastrowid

cursor.execute(query, ('English v3',))
subject2_id = cursor.lastrowid

db.commit()
# %%
# SELECT созданных предметов
cursor.execute("SELECT title FROM subjets WHERE id = %s", (subject1_id,))
print(cursor.fetchall())

cursor.execute("SELECT title FROM subjets WHERE id = %s", (subject2_id,))
print(cursor.fetchall())


# %%
# INSERT нового учебного занятия
# Создайте по два занятия для каждого предмета (lessons)
cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)", ('lesson 1 znakomstwo 2', subject1_id))
lesson1_1_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)", ('lesson 2 alfavit2', subject1_id))
lesson1_2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)", ('lesson 1 znakomstwo 2', subject2_id))
lesson2_1_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)", ('lesson 2 alfavit2', subject2_id))
lesson2_2_id = cursor.lastrowid

db.commit()
print("id всех созданных занятий:", lesson1_1_id, lesson1_2_id, lesson2_1_id, lesson2_2_id)

# %%
# SELECT созданных занятий
cursor.execute("SELECT * FROM lessons WHERE subject_id = %s", (subject1_id,))
print(cursor.fetchall())

cursor.execute("SELECT * FROM lessons WHERE subject_id = %s", (subject2_id,))
print(cursor.fetchall())


# %%
# INSERT новые оценки
# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
cursor = db.cursor()
cursor.execute("INSERT INTO marks(value, lesson_id, student_id) VALUES (%s,%s,%s)", (5, lesson1_1_id, student_id))

cursor.execute("INSERT INTO marks(value, lesson_id, student_id) VALUES (%s,%s,%s)", (3, lesson1_2_id, student_id))

cursor.execute("INSERT INTO marks(value, lesson_id, student_id) VALUES (%s,%s,%s)", (4, lesson2_1_id, student_id))

cursor.execute("INSERT INTO marks(value, lesson_id, student_id) VALUES (%s,%s,%s)", (2, lesson2_2_id, student_id))

db.commit()


# %%
# SELECT поставленных оценок
# cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
# print(cursor.fetchall())

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
for mark_id, value, lesson_id, sid in marks:
    print(f'id оценки за урок = {mark_id}, Занятие id = {lesson_id}, Оценка: {value}')

# %%
# SELECT всех данных о новом студенте
# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов 
# -- (всё одним запросом с использованием Join)

cursor = db.cursor()
query = """
select students.name,
	   	  students.second_name,
	   	  groups.title as 'nazvanie_grupy',
	   	  books.title as 'nazvanie_knigi',
	   	  subjets.title as 'predmet',
	 	  lessons.title as 'zaniatie',
	 	  marks.value as 'ocenka_studenta'
     from students
left join `groups` ON students.group_id = `groups`.id
left join books ON students.id = books.taken_by_student_id
left join marks ON students.id = marks.student_id
left join lessons ON lessons.id = marks.lesson_id
left join subjets ON subjets.id = lessons.subject_id
where students.id = %s
"""
cursor.execute(query, (student_id,))
result = cursor.fetchall()
print("все данные по студенту:" , result)


# %%
# Закрытие соединения
db.close()

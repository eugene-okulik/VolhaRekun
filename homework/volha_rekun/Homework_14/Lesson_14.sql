-- Создайте студента (student)
INSERT INTO students (name, second_name, group_id) VALUES ('Volha', 'Rekun', 1)

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('Python for beginners', 20528)
INSERT INTO books (title , taken_by_student_id) VALUES ('Magia utra', 20528)


-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date , end_date ) VALUES ('AQA_2025_spring', '01_2025', '06_2025')
UPDATE students SET group_id = 5237 WHERE name = 'Volha' AND second_name = 'Rekun'


-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Polish')
INSERT INTO subjets (title) VALUES ('English')
INSERT INTO subjets (title) VALUES ('Spanish')

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id ) VALUES ('lesson 1 znakomstwo', 10820)
INSERT INTO lessons (title, subject_id ) VALUES ('lesson 2 alfavit', 10820)

INSERT INTO lessons (title, subject_id ) VALUES ('lesson 1 znakomstwo', 10821)
INSERT INTO lessons (title, subject_id ) VALUES ('lesson 2 alfavit', 10821)

INSERT INTO lessons (title, subject_id ) VALUES ('lesson 1 znakomstwo', 10822)
INSERT INTO lessons (title, subject_id ) VALUES ('lesson 2 alfavit', 10822)


-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id , student_id) VALUES (5, 11231, 20528)
INSERT INTO marks (value, lesson_id , student_id) VALUES (4, 11232, 20528)

INSERT INTO marks (value, lesson_id , student_id) VALUES (5, 11233, 20528)
INSERT INTO marks (value, lesson_id , student_id) VALUES (5, 11234, 20528)

INSERT INTO marks (value, lesson_id , student_id) VALUES (5, 11235, 20528)
INSERT INTO marks (value, lesson_id , student_id) VALUES (5, 11236, 20528)


-- Получите информацию из базы данных:

-- Все оценки студента
select value, lesson_id from marks where student_id = 20528

-- Все книги, которые находятся у студента
select title from books where taken_by_student_id = 20528


-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
-- (всё одним запросом с использованием Join)
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

where students.id = 20528

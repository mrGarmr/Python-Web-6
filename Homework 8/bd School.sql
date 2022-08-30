create table subject
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name Varchar(20)
);

create table groupes 
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name Varchar(5)
);

create table teacher
( 
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
full_name Varchar(40),
id_subject INTEGER references subject (id) on update cascade
);

create table student
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
full_name Varchar(40),
id_groupes INTEGER references groupes (id) on update cascade,
constraint unique_student unique (id, id_groupes)
);

create table groupes_to_subjects
(
id_groupes INTEGER references groupes (id) on update cascade,
id_subject INTEGER references subject (id) on update cascade,
primary key (id_groupes, id_subject),
constraint unique_subject unique (id_groupes, id_subject)
);

create table students_marks(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
id_student INTEGER references student (id) on update cascade,
id_groupes INTEGER references groupes (id) on update cascade,
id_subject INTEGER references subject (id) on update cascade,
mark INTEGER,
date_mark date
);


INSERT INTO groupes (name)
VALUES ('E2101'), ('E2102'), ('C2121'), ('C2122'), ('F2131'), ('F2132');

INSERT  INTO subject (name)
VALUES ('Physics'), ('Mathematics'), ('Methemathic analize'), ('Geometry'), ('Computing');

INSERT  INTO student (full_name, id_groupes)
VALUES ('Gregory Adams', '1'),('Kenneth Diaz MD', '1'),('Glenda Curtis', '1'),('Jennifer Hernandez', '1'),('Eric Williams', '1'),
('Steven Herring', '2'),('Diana Thomas', '2'),('Samuel Stewart', '2'),('Mckenzie Mccormick', '2'),('Amanda Ashley', '2'),
('Howard Barnes', '3'),('Connie Mcpherson', '3'),('Cynthia Santana', '3'),('Adam Frye', '3'),('Andrew Hicks', '3'),
('Marcus Lopez', '4'),('Michael Perez', '4'),('Daniel Smith', '4'),('Gary Carter', '4'),('Dwayne Perry', '4'),
('Stephanie Clark', '5'),('Scott Harrison', '5'),('Michelle Allen', '5'),('Keith Kennedy', '5'),('Ashley Diaz', '5'),
('Jessica Smith', '6'),('Barry Knight', '6'),('Andrew Hunter', '6'),('Michael Aguilar', '6'),('Amanda Summers', '6');

insert into teacher (full_name, id_subject)
VALUES ('Natalie Norton', '1'),('Heather Hensley', '2'),('Michael Franklin', '3'),('Hannah White', '4'),('Alexa Cook', '5');

insert into groupes_to_subjects (id_groupes, id_subject)
values (1, 1),(1, 2),(1, 3),
(2, 2),(2, 3),(2, 4),
(3, 3),(3, 4),(3, 5),
(4, 4),(4, 5),(4, 1),
(5, 5),(5, 1),(5, 2),
(6, 1),(6, 2),(6, 3);


insert into students_marks(id_student, id_groupes, id_subject, mark, date_mark )
values (1, 1, 1, 70, '2021-08-22'), (1, 1,  1, 52, '2021-08-09'), (1, 1,  1, 76, '2021-08-18'), (1, 1,  2, 100, '2021-08-30'), (1, 1,  2, 96, '2021-08-31'), (1, 1,  2, 91, '2021-08-08'), (1, 1,  3, 35, '2021-08-07'), (1, 1,  3, 41, '2021-08-16'), (1, 1,  3, 91, '2021-08-09'),
(2, 1, 1, 59, '2021-08-09'), (2, 1,  1, 61, '2021-08-14'), (2,  1, 1, 100, '2021-08-16'), (2, 1,  2, 58, '2021-09-01'), (2, 1,  2, 60, '2021-08-09'), (2, 1,  2, 65, '2021-08-13'), (2, 1,  3, 39, '2021-08-10'), (2, 1,  3, 77, '2021-08-17'), (2, 1,  3, 96, '2021-09-02'),
(3, 1,  1, 93, '2021-08-25'), (3, 1,  1, 78, '2021-08-17'), (3, 1, 1, 55, '2021-08-31'), (3, 1,  2, 56, '2021-08-17'), (3, 1,  2, 99, '2021-08-10'), (3, 1,  2, 49, '2021-08-26'), (3, 1,  3, 44, '2021-09-01'), (3, 1,  3, 41, '2021-08-18'), (3, 1,  3, 68, '2021-08-31'),
(4, 1,  1, 77, '2021-08-29'), (4, 1,  1, 69, '2021-08-18'), (4,  1, 1, 87, '2021-08-15'), (4, 1,  2, 53, '2021-08-30'), (4, 1,  2, 73, '2021-09-01'), (4, 1,  2, 59, '2021-09-02'), (4, 1,  3, 38, '2021-09-04'), (4, 1,  3, 78, '2021-08-25'), (4, 1,  3, 92, '2021-08-18'),
(5, 1,  1, 51, '2021-09-04'), (5, 1,  1, 78, '2021-09-03'), (5, 1, 1, 98, '2021-08-26'), (5, 1,  2, 81, '2021-08-29'), (5, 1,  2, 47, '2021-08-10'), (5, 1,  2, 48, '2021-08-31'), (5, 1,  3, 55, '2021-08-26'), (5, 1,  3, 34, '2021-08-21'), (5, 1,  3, 86, '2021-09-02'),
(6, 2,  4, 82, '2021-08-10'), (6, 2,  4, 93, '2021-09-03'), (6, 2, 4, 96, '2021-08-24'), (6, 2,  2, 89, '2021-08-31'), (6, 2,  2, 95, '2021-08-26'), (6, 2,  2, 33, '2021-08-27'), (6, 2,  3, 30, '2021-08-19'), (6, 2,  3, 69, '2021-08-30'), (6, 2,  3, 87, '2021-09-04'),
(7, 2, 4, 30, '2021-08-20'), (7, 2,  4, 80, '2021-08-09'), (7, 2,  4, 90, '2021-09-05'), (7, 2,  2, 73, '2021-09-04'), (7, 2,  2, 89, '2021-08-09'), (7, 2,  2, 67, '2021-08-11'), (7, 2,  3, 84, '2021-09-04'), (7, 2,  3, 38, '2021-08-28'), (7, 2,  3, 86, '2021-08-24'),
(8, 2,  4, 66, '2021-09-01'), (8, 2, 4, 60, '2021-08-24'), (8, 2,  4, 82, '2021-08-13'), (8, 2,  2, 43, '2021-08-09'), (8, 2,  2, 74, '2021-09-03'), (8, 2,  2, 91, '2021-08-25'), (8, 2,  3, 46, '2021-09-01'), (8, 2,  3, 95, '2021-08-14'), (8, 2,  3, 95, '2021-08-07'),
(9, 2, 4, 54, '2021-08-22'), (9, 2,  4, 90, '2021-08-23'), (9, 2,  4, 36, '2021-08-11'), (9, 2,  2, 84, '2021-08-13'), (9, 2,  2, 79, '2021-08-22'), (9, 2,  2, 34, '2021-09-04'), (9, 2,  3, 42, '2021-08-21'), (9, 2,  3, 81, '2021-09-02'), (9, 2,  3, 80, '2021-08-31'),
(10, 2,  4, 90, '2021-08-15'), (10, 2,  4, 61, '2021-08-21'), (10, 2,  4, 36, '2021-08-20'), (10, 2,  2, 35, '2021-08-16'), (10, 2,  2, 63, '2021-08-10'), (10, 2,  2, 46, '2021-08-14'), (10, 2,  3, 76, '2021-08-08'), (10, 2,  3, 54, '2021-08-08'), (10, 2,  3, 30, '2021-08-23'),
(11, 3,  4, 86, '2021-08-28'), (11, 3,  4, 57, '2021-08-30'), (11, 3,  4, 75, '2021-08-21'), (11, 3,  5, 52, '2021-08-13'), (11, 3,  5, 34, '2021-09-03'), (11, 3,  5, 30, '2021-09-05'), (11, 3,  3, 100, '2021-09-04'), (11, 3,  3, 56, '2021-08-31'), (11, 3,  3, 88, '2021-08-31'),
(12, 3,  4, 41, '2021-08-12'), (12, 3,  4, 69, '2021-08-10'), (12, 3,  4, 40, '2021-08-11'), (12, 3,  5, 64, '2021-08-29'), (12, 3,  5, 92, '2021-09-02'), (12, 3,  5, 82, '2021-08-08'), (12, 3,  3, 69, '2021-08-19'), (12, 3,  3, 82, '2021-08-10'), (12, 3,  3, 69, '2021-08-30'),
(13, 3,  4, 76, '2021-08-29'), (13, 3,  4, 98, '2021-08-24'), (13, 3,  4, 86, '2021-08-31'), (13, 3,  5, 35, '2021-09-01'), (13, 3,  5, 34, '2021-08-16'), (13, 3,  5, 45, '2021-08-22'), (13, 3,  3, 81, '2021-09-01'), (13, 3,  3, 69, '2021-08-19'), (13, 3,  3, 64, '2021-08-22'),
(14, 3,  4, 83, '2021-08-14'), (14, 3,  4, 47, '2021-08-28'), (14, 3,  4, 83, '2021-08-29'), (14, 3,  2, 44, '2021-08-22'), (14, 3,  5, 40, '2021-08-20'), (14, 3,  5, 42, '2021-08-15'), (14, 3,  3, 75, '2021-08-08'), (14, 3,  3, 73, '2021-08-09'), (14, 3,  3, 63, '2021-08-22'),
(15, 3,  4, 81, '2021-08-22'), (15, 3,  4, 31, '2021-08-12'), (15, 3,  4, 38, '2021-08-25'), (15, 3,  5, 48, '2021-08-25'), (15, 3,  5, 72, '2021-09-01'), (15, 3,  5, 77, '2021-08-27'), (15, 3,  3, 79, '2021-08-26'), (15, 3,  3, 77, '2021-08-14'), (15, 3,  3, 78, '2021-08-23'),
(16, 4,  1, 81, '2021-08-30'), (16, 4,  1, 94, '2021-08-21'), (16, 4,  1, 30, '2021-08-24'), (16, 4,  4, 45, '2021-08-25'), (16, 4,  4, 86, '2021-09-03'), (16, 4,  4, 87, '2021-09-04'), (16, 4,  5, 49, '2021-08-13'), (16, 4,  5, 36, '2021-08-29'), (16, 4,  5, 62, '2021-08-13'),
(17, 4,  1, 82, '2021-08-15'), (17, 4,  1, 62, '2021-08-17'), (17, 4,  1, 97, '2021-08-18'), (17, 4,  4, 77, '2021-09-01'), (17, 4,  4, 82, '2021-08-13'), (17, 4,  4, 49, '2021-08-31'), (17, 4,  5, 83, '2021-08-07'), (17, 4,  5, 76, '2021-08-08'), (17, 4,  5, 83, '2021-08-15'),
(18, 4,  1, 38, '2021-09-05'), (18, 4,  1, 95, '2021-08-27'), (18, 4,  1, 35, '2021-08-25'), (18, 4,  4, 49, '2021-09-01'), (18, 4,  4, 94, '2021-08-10'), (18,  4, 4, 87, '2021-08-09'), (18,  4, 5, 58, '2021-08-14'), (18, 4,  5, 50, '2021-08-13'), (18, 4,  5, 96, '2021-08-08'),
(19, 4,  1, 53, '2021-08-10'), (19, 4,  1, 91, '2021-08-25'), (19, 4,  1, 60, '2021-09-01'), (19, 4,  4, 95, '2021-08-26'), (19, 4,  4, 94, '2021-08-21'), (19, 4,  4, 30, '2021-08-19'), (19, 4,  5, 65, '2021-08-08'), (19, 4,  5, 78, '2021-08-19'), (19, 4,  5, 87, '2021-09-05'),
(20, 4,  1, 79, '2021-08-11'), (20, 4,  1, 92, '2021-08-28'), (20, 4,  1, 90, '2021-08-26'), (20, 4,  4, 43, '2021-08-18'), (20, 4,  4, 98, '2021-09-02'), (20, 4,  4, 66, '2021-08-24'), (20, 4,  5, 50, '2021-09-05'), (20, 4,  5, 90, '2021-09-03'), (20, 4,  5, 100, '2021-08-12'),
(21, 5,  1, 60, '2021-08-19'), (21, 5,  1, 54, '2021-08-16'), (21, 5,  1, 57, '2021-08-15'), (21, 5,  2, 95, '2021-08-07'), (21, 5,  2, 85, '2021-08-20'), (21, 5,  2, 100, '2021-08-09'), (21, 5,  5, 56, '2021-09-05'), (21, 5,  5, 67, '2021-08-31'), (25, 5,  3, 88, '2021-08-22'),
(22, 5,  1, 77, '2021-08-29'), (22, 5,  1, 98, '2021-08-10'), (22, 5,  1, 54, '2021-08-29'), (22, 5,  2, 56, '2021-08-31'), (22, 5,  2, 33, '2021-08-14'), (22, 5,  2, 40, '2021-08-10'), (22, 5,  5, 50, '2021-08-16'), (22, 5,  5, 65, '2021-08-22'), (25, 5,  3, 81, '2021-08-11'),
(23, 5,  1, 31, '2021-08-30'), (23, 5,  1, 94, '2021-08-07'), (23, 5,  1, 92, '2021-08-30'), (23, 5,  2, 31, '2021-08-26'), (23, 5,  2, 34, '2021-08-25'), (23, 5,  2, 56, '2021-09-05'), (23, 5,  5, 73, '2021-09-05'), (23, 5,  5, 83, '2021-08-09'), (25, 5,  3, 95, '2021-08-09'),
(24, 5,  1, 83, '2021-08-27'), (24, 5,  1, 35, '2021-08-25'), (24, 5,  1, 52, '2021-09-02'), (24,  5, 2, 54, '2021-08-14'), (24, 5,  2, 32, '2021-08-27'), (24, 5,  2, 81, '2021-09-03'), (24, 5,  5, 86, '2021-08-23'), (24, 5,  5, 59, '2021-08-10'), (25, 5,  3, 48, '2021-08-31'),
(25,  5, 1, 74, '2021-08-18'), (25, 5,  1, 100, '2021-08-31'), (25, 5,  1, 48, '2021-08-24'), (25, 5,  2, 56, '2021-08-10'), (25, 5,  2, 69, '2021-08-31'), (25, 5,  2, 99, '2021-08-08'), (25, 5,  5, 34, '2021-09-03'), (25, 5,  5, 79, '2021-08-31'), (25, 5,  5, 56, '2021-08-26'),
(26, 6,  1, 60, '2021-09-04'), (26,6,   1, 76, '2021-08-18'), (26, 6,  1, 64, '2021-09-02'), (26, 6,  2, 66, '2021-08-11'), (26, 6,  2, 67, '2021-08-28'), (26, 6,  2, 62, '2021-09-01'), (26, 6,  3, 57, '2021-09-01'), (26, 6,  3, 59, '2021-09-02'), (26, 6,  3, 90, '2021-08-11'),
(27, 6,  1, 55, '2021-09-01'), (27, 6,  1, 68, '2021-08-19'), (27, 6,  1, 59, '2021-08-19'), (27, 6,  2, 88, '2021-08-10'), (27, 6,  2, 89, '2021-08-29'), (27, 6,  2, 40, '2021-08-07'), (27, 6,  3, 79, '2021-08-23'), (27, 6,  3, 49, '2021-08-11'), (27, 6,  3, 40, '2021-09-01'),
(28, 6,  1, 35, '2021-08-09'), (28, 6,  1, 86, '2021-09-03'), (28, 6,  1, 83, '2021-08-20'), (28, 6,  2, 40, '2021-08-19'), (28, 6,  2, 76, '2021-08-29'), (28, 6,  2, 91, '2021-08-18'), (28, 6,  3, 45, '2021-09-04'), (28, 6,  3, 94, '2021-08-21'), (28, 6,  3, 92, '2021-08-17'),
(29, 6,  1, 71, '2021-08-08'), (29, 6,  1, 34, '2021-08-12'), (29, 6,  1, 53, '2021-08-08'), (29, 6,  2, 35, '2021-08-21'), (29, 6,   2, 87, '2021-08-19'), (29, 6,  2, 83, '2021-08-29'), (29, 6,  3, 99, '2021-08-08'), (29, 6,  3, 94, '2021-09-01'), (29, 6,  3, 41, '2021-08-29'),
(30, 6,  1, 97, '2021-08-29'), (30, 6,  1, 87, '2021-09-05'), (30, 6,  1, 97, '2021-08-17'), (30, 6,  2, 97, '2021-08-12'), (30, 6,  2, 33, '2021-08-27'), (30, 6,  2, 39, '2021-08-19'), (30, 6,  3, 34, '2021-08-14'), (30, 6,  3, 83, '2021-08-31'), (30, 6,  3, 54, '2021-08-07')
;


--5 студентов с наибольшим средним баллом по всем предметам.
select student.full_name, marks.average_mark
from student 
join 
(select id_student,  avg(mark)  as average_mark
from students_marks  
group by id_student 
order by average_mark desc
limit 5) as marks on student.id = marks.id_student
order by marks.average_mark desc;

--1 студент с наивысшим средним баллом по одному предмету.

select student.full_name, subjs.name, marks.average_mark
from student
join 
(select id_student, id_subject, avg(mark)  as average_mark
from students_marks  
group by id_student, id_subject
order by average_mark desc
limit 1) as marks on student.id = marks.id_student
join subject as subjs on subjs.id = marks.id_subject
order by marks.average_mark desc;

--средний балл в группе по одному предмету.

select groupes.id, groupes.name, subject.name, marks.average_mark
from groupes
join 
(select id_groupes, id_subject, avg(mark)  as average_mark
from students_marks  
group by id_groupes , id_subject ) as marks on groupes.id = marks.id_groupes
join subject on subject.id = marks.id_subject
order by marks.average_mark desc;

--Средний балл в потоке.
select avg(mark)  as average_mark
from students_marks  
order by average_mark desc
limit 1
;
--Какие курсы читает преподаватель.

select teacher.full_name , subject.name 
from teacher 
join subject on subject.id = teacher.id_subject 
where teacher.full_name='Natalie Norton'
;

--Список студентов в группе.
select student.full_name
from student 
join groupes as g on student.id_groupes = g.id
where g.name = 'E2102'
;

--Оценки студентов в группе по предмету.
select st.full_name, sm.mark
from students_marks as sm 
join groupes as g on g.id = sm.id_groupes 
join subject as sj on sj.id = sm.id_subject
join student as st on st.id = sm.id_student
where g.name = 'E2102' 
and sj.name = 'Mathematics'
order by  st.full_name
;

--Оценки студентов в группе по предмету на последнем занятии.
select st.full_name, sm.mark, sj.name,  g.name, sm.date_mark 
from students_marks as sm 
join (
select id_groupes , id_subject, max(date_mark) as max_date 
from students_marks  
group by id_groupes , id_subject, id_student
) 
as sm_date on (sm.id_groupes , sm.id_subject, sm.date_mark ) = (sm_date.id_groupes, sm_date.id_subject, sm_date.max_date)
join subject as sj on sj.id = sm.id_subject
join student as st on st.id = sm.id_student
join groupes  as g on g.id = sm.id_groupes
where g.name = 'E2102' 
and sj.name = 'Mathematics'
 ;
--Список курсов, которые посещает студент.

select  st.full_name, gr.name, sj.name
from groupes_to_subjects as gts
join subject as sj on sj.id = gts.id_subject 
join groupes as gr on gts.id_groupes = gr.id 
join 
(select full_name, id_groupes 
from student where full_name = 'Diana Thomas'
) as st on st.id_groupes = gts.id_groupes 
;

--Список курсов, которые студенту читает преподаватель.

select sub.name, st.full_name, t.full_name 
from students_marks sm 
join teacher t on sm.id_subject = t.id_subject 
join student st on sm.id_student = st.id 
join subject sub on sm.id_subject = sub.id 
where t.full_name = 'Heather Hensley' and st.full_name = 'Diana Thomas'
group by sub.name, st.full_name, t.full_name;


--Средний балл, который преподаватель ставит студенту.
select avg(sm.mark), sub.name, st.full_name, t.full_name 
from students_marks sm 
join teacher t on sm.id_subject = t.id_subject 
join student st on sm.id_student = st.id 
join subject sub on sm.id_subject = sub.id 
where t.full_name = 'Heather Hensley' and st.full_name = 'Diana Thomas'
group by sub.name, st.full_name, t.full_name;

--Средний балл, который ставит преподаватель.
select avg(sm.mark), t.full_name
from students_marks as sm 
join teacher t on sm.id_subject = t.id_subject 
where t.full_name = 'Heather Hensley'
group by  t.full_name
;
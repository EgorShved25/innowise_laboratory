-- Создание таблиц
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Вставка данных студентов
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Вставка оценок
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- Запросы для анализа данных

-- 1. Все оценки студента по имени Alice Johnson
SELECT g.*
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 2. Средний балл каждого студента
SELECT s.id, s.full_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

-- 3. Все студенты, родившиеся после 2004
SELECT * FROM students WHERE birth_year > 2004;

-- 4. Все предметы и их средние оценки
SELECT subject, AVG(grade) AS avg_grade
FROM grades
GROUP BY subject;

-- 5. Топ 3 студентов с наивысшими средними оценками
SELECT s.id, s.full_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 6. Студенты, у которых есть оценка ниже 80 в каком-либо предмете
SELECT DISTINCT s.id, s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;
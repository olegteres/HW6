class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = []

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def culc_average_grade(self):
        grade_list = []
        for grade in self.grades.values():
            for i in grade:
                grade_list.append(i)
        self.average_grade = sum(grade_list) / len(grade_list)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade}\n" \
               f"Курсы в процессе изучения:{self.courses_in_progress}\n" f"Завершенные курсы: {self.finished_courses}"

    def __lt__(some_student, other_student):
        return some_student.average_grade < other_student.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = []
        self.courses_attached = []

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)

    def culc_average_grade(self):
        grade_list = []
        for grade in self.grades.values():
            for i in grade:
                grade_list.append(i)
        self.average_grade = sum(grade_list) / len(grade_list)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade}"

    def __lt__(some_lecturer, other_lecturer):
        return some_lecturer.average_grade < other_lecturer.average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)

    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


Ivan_Petrov = Student("Иван", "Петров", "мужчина")
Elena_Kononova = Student("Елена", "Кононова", "женщина")

Sergey_Grigoryev = Lecturer("Сергей", "Григорьев")
Mariya_Mikhaylova = Lecturer("Мария", "Михайлова")

Artur_Derbin = Reviewer("Артур", "Дербин")
Olga_Golubeva = Reviewer("Ольга", "Голубева")

Sergey_Grigoryev.add_courses_attached("Python")
Sergey_Grigoryev.add_courses_attached("Git")

Mariya_Mikhaylova.add_courses_attached("Python")
Mariya_Mikhaylova.add_courses_attached("Git")

Artur_Derbin.add_courses_attached("Python")
Artur_Derbin.add_courses_attached("Git")

Olga_Golubeva.add_courses_attached("Python")
Olga_Golubeva.add_courses_attached("Git")

Ivan_Petrov.add_finished_courses("Введение в программирование")
Ivan_Petrov.add_courses_in_progress("Python")
Ivan_Petrov.add_courses_in_progress("Git")

Elena_Kononova.add_finished_courses("Введение в программирование")
Elena_Kononova.add_courses_in_progress("Python")
Elena_Kononova.add_courses_in_progress("Git")

Artur_Derbin.rate_homework(Ivan_Petrov, "Python", 6)
Artur_Derbin.rate_homework(Ivan_Petrov, "Git", 3)

Olga_Golubeva.rate_homework(Elena_Kononova, "Python", 4)
Olga_Golubeva.rate_homework(Elena_Kononova, "Git", 9)

Ivan_Petrov.rate_lecture(Sergey_Grigoryev, "Python", 5)
Ivan_Petrov.rate_lecture(Mariya_Mikhaylova, "Git", 10)

Elena_Kononova.rate_lecture(Sergey_Grigoryev, "Python", 7)
Elena_Kononova.rate_lecture(Mariya_Mikhaylova, "Git", 8)

Ivan_Petrov.culc_average_grade()
Elena_Kononova.culc_average_grade()
Sergey_Grigoryev.culc_average_grade()
Mariya_Mikhaylova.culc_average_grade()

print(Ivan_Petrov)
print()
print(Elena_Kononova)
print()
print(Sergey_Grigoryev)
print()
print(Mariya_Mikhaylova)
print()

if Ivan_Petrov < Elena_Kononova:
    print("Иван Петров имеет среднюю оценку хуже, чем  Елена Кононова")
else:
    print("Иван Петров имеет среднюю оценку лучше, чем  Елена Кононова")
print()

if Mariya_Mikhaylova < Sergey_Grigoryev:
    print("Мария Михайлова имеет среднюю оценку хуже, чем  Сергей Григорьев")
else:
    print("Мария Михайлова имеет среднюю оценку лучше, чем  Сергей Григорьев")
print()

students_list = [Ivan_Petrov, Elena_Kononova]
lecturers_list = [Sergey_Grigoryev, Mariya_Mikhaylova]


def students_average_grade(students, course):
    grades_list = []
    for student in students:
        if student.grades.get(course) != None:
            for i in student.grades.get(course):
                grades_list.append(i)
        else:
            return "Ошибка"
    students_average_grade = sum(grades_list) / len(grades_list)
    return f"Средняя оценка всех студентов на курсе: {students_average_grade}"


def lecturers_average_grade(lecturers, course):
    grades_list = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            for i in lecturer.grades.get(course):
                grades_list.append(i)
    lecturers_average_grade = sum(grades_list) / len(grades_list)
    return f"Средняя оценка всех преподавателей на курсе:{lecturers_average_grade}"


print(students_average_grade(students_list, course="Git"))
print(students_average_grade(students_list, course="Python"))

print(lecturers_average_grade(lecturers_list, course="Git"))
print(lecturers_average_grade(lecturers_list, course="Python"))
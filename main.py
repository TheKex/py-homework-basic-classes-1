class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' + \
               f'Средняя оценка за домашние задания: {self.__get_avg_grades__()}\n' + \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' + \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __get_avg_grades__(self):
        grades_total_sum, grades_total_len = 0, 0

        for grades in self.grades.values():
            grades_total_sum += sum(grades)
            grades_total_len += len(grades)
        return grades_total_sum / grades_total_len if grades_total_len != 0 else None

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__get_avg_grades__() < other.__get_avg_grades__()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__get_avg_grades__() == other.__get_avg_grades__()

    def rate_lecturer_course(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.ratings:
                lecturer.ratings[course] += [grade]
            else:
                lecturer.ratings[course] = [grade]
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}

    def __str__(self):
        return super().__str__() + f'\nСредняя оценка за лекции: {self.__get_avg_rate__()}'

    def __get_avg_rate__(self):
        total_raiting_sum, total_raiting_len = 0, 0
        for raiting in self.ratings.values():
            total_raiting_sum += sum(raiting)
            total_raiting_len += len(raiting)

        return total_raiting_sum / total_raiting_len if total_raiting_len != 0 else None

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__get_avg_rate__() < other.__get_avg_rate__()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return  self.__get_avg_rate__() == other.__get_avg_rate__()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


first_student = Student('Alex', 'Tomilin', 'Male')
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Python']
first_student.grades['Python'] = [5, 3, 5]
first_student.grades['Git'] = [8]
print('*** ПЕРВЫЙ СТУДЕНТ ***')
print(first_student)

second_student = Student('Egor', 'Savin', 'Helicopter')
second_student.courses_in_progress += ['Git', 'JavaScript']
second_student.finished_courses += ['Python', 'HTML']
second_student.grades['Python'] = [5, 9, 5]
second_student.grades['Git'] = [8, 10]
print('\n*** ВТОРОЙ СТУДЕНТ ***')
print(second_student)

first_lecturer = Lecturer('Ivan', 'Ivanov')
first_lecturer.courses_attached += ['Git']
print('\n*** ПЕРВЫЙ ЛЕКТОР ***')
print(first_lecturer)

second_lecturer = Lecturer('Andrey', 'Petrov')
second_lecturer.courses_attached += ['JavaScript']
print('\n*** ВТОРОЙ ЛЕКТОР ***')
print(second_lecturer)

first_reviewer = Reviewer('Tima', 'Tomilin')
first_reviewer.courses_attached += ['Git']
print('\n*** ПЕРВЫЙ ЭКСПЕРТ ***')
print(first_reviewer)

second_reviewer = Reviewer('Andrey', 'Petrov')
second_reviewer.courses_attached += ['JavaScript']
print('\n*** ВТОРОЙ ЭКСПЕРТ ***')
print(second_reviewer)

first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 7)

print('\n*** ПЕРВЫЙ СТУДЕНТ ***')
print(first_student)
print('\n*** ВТОРОЙ СТУДЕНТ ***')
print(second_student)

second_reviewer.rate_hw(second_student, 'JavaScript', 10)

print('\n*** ВТОРОЙ СТУДЕНТ ***')
print(second_student)

first_student.rate_lecturer_course(first_lecturer, 'Git', 10)
second_student.rate_lecturer_course(first_lecturer, 'Git', 10)

second_student.rate_lecturer_course(second_lecturer, 'JavaScript', 6)
print('\n*** ПЕРВЫЙ ЛЕКТОР ***')
print(first_lecturer)

print('\n*** ВТОРОЙ ЛЕКТОР ***')
print(second_lecturer)

print('first_lecturer < second_lecturer :', first_lecturer < second_lecturer)
print('first_lecturer > second_lecturer :', first_lecturer > second_lecturer)
print('first_lecturer == second_lecturer :', first_lecturer < second_lecturer)

print('\n*** ПЕРВЫЙ СТУДЕНТ ***')
print(first_student)
print('\n*** ВТОРОЙ СТУДЕНТ ***')
print(second_student)
print('first_student < second_student :', first_student < second_student)
print('first_student > second_student :', first_student > second_student)
print('first_student == second_student :', first_student == second_student)


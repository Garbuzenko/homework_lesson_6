class Stat:
    def __str__(self):
        # res = "\n" + "-"*10
        res = f"\n{self.__class__}";
        res += f"\nИмя: {self.name}";
        res += f"\nФамилия: {self.surname}";
        return res;

    def __lt__(self, obj):
        if self.avg() < obj.avg():
            res = True;
        else:
            res = False;
        return res;

    def avg(self):
        i_grade = 0;
        sum_grade = 0;
        for key, grade in self.grades.items():
            for value in grade:
                sum_grade += value
                i_grade += 1
        if i_grade != 0:
            return sum_grade / i_grade

class Student(Stat):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}



    def __str__(self):
        res = super().__str__()
        res += f"\nСредняя оценка за домашние задания: {self.avg()}"
        res += f"\nКурсы в процессе изучения: {self.courses_in_progress}"
        res += f"\nЗавершенные курсы: {self.finished_courses}"
        return res



    def rate_l(self, lect, course, grade):
        if not (grade >=0 and grade <= 10):
            return 'Ошибка'

        if isinstance(lect, Lecturer) and course in lect.courses_attached and course in self.courses_in_progress:
            if course in lect.grades:
                lect.grades[course] += [grade]
            else:
                lect.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor(Stat):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        res = super().__str__()
        res += f"\nСредняя оценка за лекции: {self.avg()}"
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python', 'Java', 'DS']
best_student.finished_courses += ['JS']

ordinary_student = Student('Peter', 'Parker', 'man')
ordinary_student.courses_in_progress += ['Python', 'JS']
ordinary_student.finished_courses += ['DS']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'JS']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(ordinary_student, 'Python', 7)

ordinary_reviewer = Reviewer('Ivan', 'Ivanov')
ordinary_reviewer.courses_attached += ['JS']
ordinary_reviewer.rate_hw(ordinary_student, 'JS', 9)

cool_lector = Lecturer('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

ordinary_lector = Lecturer('Ivan', 'Ivanov')
ordinary_lector.courses_attached += ['JS']

cool_reviewer.rate_hw(ordinary_student, 'JS', 8)

best_student.rate_l(cool_lector, 'Python', 9)
best_student.rate_l(cool_lector, 'Python', 10)
ordinary_student.rate_l(ordinary_lector, 'JS', 5)

print(best_student)
print(ordinary_student)
print(cool_lector)
print(ordinary_lector)
print(cool_reviewer)

print(best_student > ordinary_student)
print(cool_lector < ordinary_lector)
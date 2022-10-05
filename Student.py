class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_s = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade]
            else:
                lecturer.grades_l[course] = [grade]
        else:
            return 'Error'
    
    def middle_grade(self):
        self.mid = round(sum(sum(self.grades_s.values(), [])) / len(sum(self.grades_s.values(), [])), 1)
        return self.mid

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.middle_grade() < other.middle_grade()
        return 'Enter the correct data!'

    def __str__(self):
        string = f'''Name: {self.name} \nSurname: {self.surname}
Avarage grade for homework: {self.middle_grade()} \nCourses in progress: {", ".join(self.courses_in_progress)} \nCompleted courses: {", ".join(self.finished_courses)}'''
        return string

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_l = {}
    
    def middle_grade(self):
        self.mid = round(sum(sum(self.grades_l.values(), [])) / len(sum(self.grades_l.values(), [])), 1)
        return self.mid

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.middle_grade() < other.middle_grade()
        return 'Enter the correct data!'
    
    def __str__(self):
        string = f'''Name: {self.name} \nSurname: {self.surname} \nAvarage grade for lecture: {self.middle_grade()}'''
        return string

    
class Rewiever(Mentor):
    def rate_s(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades_s:
                student.grades_s[course] += [grade]
            else:
                student.grades_s[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        string = f'''Name: {self.name} \nSurname: {self.surname}'''
        return string


high_skill_student = Student('Diego', 'Maradona', 'male')
low_skill_student = Student('Alexandr', 'Kerzhakov', 'male')
high_skill_student.courses_in_progress += ['Python']
low_skill_student.courses_in_progress += ['Python']
high_skill_student.finished_courses += ['Introduction to programming']
low_skill_student.finished_courses += ['Introduction to programming']

any_lecturer = Lecturer('Hannibal', 'Lecter')
some_lecturer = Lecturer('Gregory', 'House')
any_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Python']

any_rewiever = Rewiever('Uncle', 'Stepa')
some_rewiever = Rewiever('Grandpa', 'Maxim')
some_rewiever.courses_attached += ['Python']
any_rewiever.courses_attached += ['Python']

high_skill_student.rate_l(any_lecturer, 'Python', 10)
high_skill_student.rate_l(some_lecturer, 'Python', 9)
low_skill_student.rate_l(any_lecturer, 'Python', 10)
low_skill_student.rate_l(some_lecturer, 'Python', 8)

any_rewiever.rate_s(high_skill_student, 'Python', 10)
any_rewiever.rate_s(high_skill_student, 'Python', 10)
some_rewiever.rate_s(high_skill_student, 'Python', 10)
any_rewiever.rate_s(low_skill_student, 'Python', 6)
some_rewiever.rate_s(low_skill_student, 'Python', 7)
some_rewiever.rate_s(low_skill_student, 'Python', 6)

print(some_rewiever)
print(any_rewiever)

high_skill_student.middle_grade()
low_skill_student.middle_grade()
print('High skill was better!' if high_skill_student > low_skill_student else 'Low skill was better!')
print(high_skill_student)
print(low_skill_student)

any_lecturer.middle_grade()
some_lecturer.middle_grade()
print('Some lecturer was better here' if any_lecturer < some_lecturer else 'Any lecturer was better here!')
print(some_lecturer)
print(any_lecturer)

students_list = [high_skill_student, low_skill_student]

def students_average_grade(students_list, course):
    sum, count = 0, 0
    for i in students_list:
        for c in i.grades_s[course]:
            sum += c
            count += 1
    if sum == 0 or count == 0:
        return 'Nothing'
    return int(sum/count)

print(students_average_grade(students_list, 'Python'))

def lecture_average_grade(students_list, course):
    sum, count = 0, 0
    for i in students_list:
        for c in i.grades_s[course]:
            sum += c
            count += 1
    if sum == 0 or count == 0:
        return 'Nothing'
    return int(sum/count)

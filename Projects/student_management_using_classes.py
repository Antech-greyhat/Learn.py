class Student:
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores
    def get_average(self) -> float:
        average_class = sum(self.scores) / len(self.scores)
        return average_class

    def get_grade(self):
        class_average = self.get_average()
        if class_average >= 80:
            return 'A'
        elif class_average >= 65:
            return 'B'
        elif class_average >= 50:
            return 'C'
        elif class_average >= 40:
            return 'D'
        else:
            return 'Failed'
    def __str__(self) -> str:
        return f"{self.name} has an Average of:{self.get_average():.1f},and Grade of:{self.get_grade()}"

student_obj = Student('antony',[90,50,60])
print(student_obj.get_average())
print(student_obj.get_grade())
print(student_obj)

class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student)

    def top_student(self):
        top_student = max(self.students, key=lambda s: s.get_average())
        return top_student

    def unique_grades(self):
        grades = set()
        for student in self.students:
            grades.add(student.get_grade())
        return grades

my_class = Classroom('Year 2')

s1 = Student('antony',[100,80,70])
s2 = Student('joshua',[100,100,90])

my_class.add_student(s1)
my_class.add_student(s2)

print(len(my_class.students))
my_class.list_students()

print(my_class.top_student())
print(my_class.unique_grades())

def create_student_safely(classroom):
    user_name = input('Enter your name:').strip()
    user_score = input('Enter your score separated by comma eg(70,56,78):')
    split_score = user_score.split(',')
    clean_scores = []

    try:
        for score in split_score:
            clean_scores.append(float(score.strip()))
    except ValueError as e:
        print(f"{e}: Score must be numbers. Student not added.")
        return
    new_student = Student(user_name,clean_scores)
    classroom.add_student(new_student)

    print(f"Success! {new_student.name} was added.")

create_student_safely(my_class)
print('---Final Report---')
my_class.list_students()
print(my_class.top_student())
print(my_class.unique_grades())
print(len(my_class.students))
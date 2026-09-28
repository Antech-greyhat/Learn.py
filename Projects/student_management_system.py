# A short capstone
import random
students = [
    {'name':'Antony','scores':[70,67,89]},
    {'name':'Joshua','scores':[77,89,67]},
    {'name':'Fridah','scores':[60,55,67]}
]
print(students)

def get_average(scores):
    average = sum(scores) / len(scores)
    return average
print(get_average([90,75,35]))

def get_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 65:
        return 'B'
    elif average >= 55:
        return 'C'
    elif average >= 45:
        return 'D'
    else:
        return 'Fail'

for student in students:
    average = get_average(student['scores'])
    grade = get_grade(average)
    print(f"{student['name']}:{average:.1f}, {grade}")


unique_grades = set()

print("\n--- Student Results ---")
for student in students:
    average = get_average(student['scores'])
    grade = get_grade(average)


    unique_grades.add(grade)

    print(f"{student['name']}: {average:.1f}, {grade}")

print(f"\nDistinct grades awarded across the class: {unique_grades}")

top_scorer = max(students, key=lambda s: get_average(s['scores']))
top_avg = get_average(top_scorer['scores'])

print(f"Top Scorer: {top_scorer['name']} with a stellar average of {top_avg:.1f}")

def add_student(students):
    user_name = input('Enter name:').strip()
    user_score = input('Enter score separated by a comma:')
    raw_score = user_score.split(',')
    clean_scores = []
    try:
        for score in raw_score:
            clean_scores.append(float(score.strip()))
    except ValueError:
        print("Error: Invalid Score Format. Please Enter Numbers only. student not added.")
        return
    students.append({
        'name':user_name,
        'scores':clean_scores
    })
    print(f"Success ! {user_name} has been added to the database.")

student_database = []
add_student(student_database)
add_student(student_database)

print('\nFinal Database State:',student_database)

student_of_the_day = random.choice(students)
print(f"\nStudent of the day:{student_of_the_day['name']}🎉")


#print(get_grade(85))
#print(get_grade(60))
#print(get_grade(50))
#print(get_grade(30))
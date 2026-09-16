students = ['antony', 'joshua', 'eliud', 'alex']
scores = [78,67,99,56]
passed_count = 0

def get_grades(score):
    if score >=90:
        return 'A'
    if score >=70:
        return 'B'
    if score >= 60:
        return 'C'
    else:
        return 'D'

for student,score in zip(students,scores):
    letter_grade = get_grades(score)
    print(f'{student} scored {score} -Grade: {letter_grade}')
    if letter_grade == 'C' or letter_grade == 'B' or letter_grade == 'A':
        passed_count += 1
print(f'{passed_count} out of {len(students)} passed')




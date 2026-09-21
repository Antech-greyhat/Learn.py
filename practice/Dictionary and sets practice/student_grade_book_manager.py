students = [
    {'name': 'Antony', 'scores': [89,80,90]},
    {'name': 'Joshua', 'scores': [100,98,80]},
    {'name': 'Eliud', 'scores': [80,70,80]}
]
print(students)

def get_average(scores):
    return sum(scores) / len(scores)

print(get_average([89,80,90]))
print(get_average([100,98,80]))
print(get_average([100,98,80]))

def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 70:
        return 'B'
    if score >= 60:
        return 'C'
    else:
        return 'D'
for student in students:
    average = get_average(students['scores'])
    grade = get_grade(average)
    print(f'{student[f'name']}: average {average:.1f}, grade {grade}')

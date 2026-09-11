
student_name = 'antony'

def generate_certificate(course_title):
    completion_message = f'Thrilled that {student_name} has successfully completed python backend'
    return completion_message

generate_certificate("Backend")
# commenting  this code out will crash the whole program since it print NameError due to function scope.

#print(completion_message) # NameError: name 'completion_message' is not defined

course_name = 'bit'

def generate_card(card):
    success_message = f"Congratulation {student_name} for completing {course_name} kudos"
    print(success_message)

generate_card('antony')

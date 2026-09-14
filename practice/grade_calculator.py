def get_grade(score):
    if score < 40:
        print('You scored an F')
    elif score <= 55:
        print('You scored a D')
    elif score <= 65:
        print('You scored a C')
    elif score <= 80:
        print('You Scored an B')
    elif score <= 100:
        print('You scored an A')
    else:
        print('Invalid score')

    local_scope_variable = 'returns an error because is a local scope variable'

    return score
get_grade(38)
get_grade(42)
get_grade(56)
get_grade(77)
get_grade(89)
get_grade(101)
#print(local_scope_variable) ;;; NameError
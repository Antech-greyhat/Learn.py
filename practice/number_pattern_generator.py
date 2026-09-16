# practice on loops and sequence
def number_pattern(n):
    if type(n) is not int or isinstance(n, bool):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))

    return " ".join(numbers)
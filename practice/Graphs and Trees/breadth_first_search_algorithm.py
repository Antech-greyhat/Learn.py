def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be At least 1'
    result = []
    queue = [('', 0, 0)]
    while queue:
        print(queue)
        current, opens_used, closes_used = queue.pop(0)

        if current == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    return  result

print(gen_parentheses(2))
print(gen_parentheses(3))
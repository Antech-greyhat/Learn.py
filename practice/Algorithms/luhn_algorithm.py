def verify_card_number(card_number):
    clean_number = card_number.replace('-', '').replace(' ', '')

    total = 0
    for i in range(len(clean_number) - 1, -1, -1):
        digit = int(clean_number[i])

        if (len(clean_number) - 1 - i) % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
def to_roman(decimal_number):
    tmp = decimal_number
    count = len(str(decimal_number))

    

    m = decimal_number//1000
    decimal_number %= 1000
    d = decimal_number // 500
    decimal_number %= 500
    c = decimal_number//100
    decimal_number %= 100
    l = decimal_number // 50
    decimal_number %= 50
    x = decimal_number//10
    decimal_number %= 10
    v = decimal_number // 5
    decimal_number %= 5
    i = decimal_number

    if decimal_number == 5:
        return 'V'
    elif decimal_number == 10:
        return 'X'
    elif decimal_number == 50:
        return 'L'
    elif decimal_number == 100:
        return 'C'
    elif decimal_number == 500:
        return 'D'
    elif decimal_number == 1000:
        return 'M'
    elif decimal_number == 2:
        return 'II'
    elif decimal_number == 3:
        return 'III'
    elif decimal_number == 4:
        return 'IV'
    return 'I'

def from_roman(roman_number):
    if roman_number == 'V':
        return 5
    if roman_number == 'X':
        return 10
    if roman_number == 'L':
        return 50
    if roman_number == 'C':
        return 100
    if roman_number == 'D':
        return 500
    if roman_number == 'M':
        return 1000
    return 1
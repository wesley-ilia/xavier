def to_roman(decimal_number):
    m = decimal_number//1000
    decimal_number %= 1000
    c = decimal_number//100
    decimal_number %= 100
    x = decimal_number//10
    decimal_number %= 10
    i = decimal_number

    if(m <= 3):
        strin = printer(m, 'M',' ',' ')
        strin +=printer(c, 'C','D','M')
        strin +=printer(x, 'X','L','C')
        strin +=printer(i, 'I','V','X')
        print(strin)
    else:
        print("invalid convert")

def from_roman2(roman_numerl):

    return

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

def printer(number,r, n, p):
    if (number == 1):
        return(r)
    elif(number == 2):
        return ("%c%c" % (r, r))
    elif(number == 3):
        return ("%c%c%c" % (r, r, r))
    elif(number == 4):
        return ("%c%c" % (r, n))
    elif(number == 5):
        return ("%c" % n),
    elif(number == 6):
        return ("%c%c" % (n, r))
    elif(number == 7):
        return ("%c%c%c" % (n, r, r))
    elif(number == 8):
        return ("%c%c%c%c" % (n, r, r, r))
    if (number == 9):
        return ("%c%c" % (r, p))
    return 


if (__name__ == "__main__"):
    print("Numeral romano")
    to_roman(1494)



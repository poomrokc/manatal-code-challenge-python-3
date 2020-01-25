"""
Manatal python Exercise 3: Algorithmic Test
Author: Poompatai Puntitpong
Note: For number more than 3000, lots of M are used
"""

import numbers

"""In case you want to add more symbols digits just add here"""
max_digit = 3
symbols = [
    ['I', 'V'],
    ['X', 'L'],
    ['C', 'D'],
    ['M']
]

def roman_digit(digit, value):
    if value == 9:
        return symbols[digit][0] + symbols[digit+1][0]
    elif value >= 5:
        return symbols[digit][1] + symbols[digit][0] * (value-5)
    elif value == 4:
        return symbols[digit][0] + symbols[digit][1]
    else:
        return symbols[digit][0] * value

def to_roman(input):
    if not isinstance(input, numbers.Number):
        raise TypeError('Input must be a number')
    if input < 0:
        raise ValueError('Input must not be negative')
    output = ''
    for digit in range(max_digit):
        output = roman_digit(digit, input % 10) + output
        input //= 10
    output = symbols[max_digit][0] * input + output
    return output

if __name__ == '__main__':
    input_number = int(input('Integer to be converted to roman numeral: '))
    print('Roman numeral representation:', to_roman(input_number))
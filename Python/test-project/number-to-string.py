import sys

dictionary = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

number: str = input("Type a number between 1 and 9999 as digits: ")
length: int = len(number)
if (length > 4 or not number.isdigit() or number.startswith('-') or number.startswith('0')):
    print('That is not a valid input.')
    sys.exit(0)

output: str = ""
i: int = 0
for digit in number:
    place = length - i
    if place == 4:
        output += dictionary.get(int(digit)) + ' '
        output += dictionary.get(int(1000)) + ' '
    elif place == 3 and digit != '0':
        output += dictionary.get(int(digit)) + ' '
        output += dictionary.get(int(100)) + ' '
    elif place == 2 and digit != '0':
        if digit == '1':
            output += dictionary.get(int(number[-2:]))
            break
        else:
            output += dictionary.get(int(digit + '0')) + ' '
    else:
        output += dictionary.get(int(digit))
    i += 1
    
print(output)
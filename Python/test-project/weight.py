print('Weight conversion function')
weight = float(input('Weight:  '))
unit = str(input('(K)g or (L)bs?:  '))
if unit.lower() == 'l':
    print('Weight in kg:', weight*0.45359237)
elif unit.lower() == 'k':
    print('Weight in lbs:', weight/0.45359237)
else:
    print('Unit was not recognized. Please enter K, or L.')
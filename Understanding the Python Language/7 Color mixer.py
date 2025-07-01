print('color mixer')

R = 'red'
B = 'blue'
Y = 'yellow'

primCol1 = input('Enter ptimary color 1:')
primCol2 = input('Enter ptimary color 2:')

purple = R + B
orange = R + Y
green = B + Y

if primCol1 == R and primCol2 == B:
    print('Purple')
elif primCol1 == R and primCol2 == Y:
    print('Orange')
elif primCol1 == B and primCol2 == Y:
    print('Green')
else:
    print('error')




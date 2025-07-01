print('Weight Calculator')

mass =float(input('Enter object mass \n'))

weight = mass * 9.8

if weight > 500 :
    print('This is overweight')
elif weight >100 :
     print('This is normal')
elif weight <100 :
    print('This is light')
else:
    print('Invalid')




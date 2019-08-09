'''DICE ROLLING SIMULATOR'''
from random import *
while(True):
    r=randint(1,6)
    print('rolling the dice')
    print(r)
    print('do u want to roll again')
    roll=input()
    if(roll=='yes' or roll=='y'):
        print('ok...rolling again')
        r=randint(1,6)
        print(r,'\n')
    else:
        print('ok...bye')
        break;




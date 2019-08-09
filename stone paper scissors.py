from random import *
l=['stone','paper','scissors']
print(l)
s=0
c=0
while(True):
    a=input('enter any one from list:')
    r=choice(l)
    print(r)
    if(r=='stone' and a=='paper'):
       print('you win\n')
       s=s+1
    elif(r=='paper' and a=='stone'):
       print('computer  win\n')
       c=c+1
    elif(r=='paper' and a=='scissors'):
       print('you win\n')
       s=s+1
    elif(r=='scissors' and a=='paper'):
       print('computer win\n')
       c=c+1
    elif(r=='stone' and a=='scissors'):
       print('computer win\n')
       c=c+1
    elif(r=='scissors' and a=='stone'):
       print('you win\n')
       s=s+1
    elif(r==a):
        print('both are same\n')
    else:
        print('please make a valid choice')
    print('do u want to play again:')
    t=input('yes or no:')
    if(t=='yes' or t=='y'):
        continue
    else :
        break
print('player scores:',s)
print('computer scores:',c)
        


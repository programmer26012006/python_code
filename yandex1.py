# _*_ coding: utf -8 _*_
print('Hi, welcome to my game')
print('My game has a few rules')
print('Rule number one: \nFollow the rules of the game')
print('Rule number two: \nif you gave the wrong answer you go back to the beginning')
print('Good luck')
print('LEVEL 1'
      '________')
x = int(input('print first any number 5 >= x <= 2 : '))
y = int(input('print second any number: 5 >= x <= 2 '))
d = 0
while d == 0:
    if (x <= 5 and x >= 2) and (y <= 5 and y >= 2):
        c = x + y
        print('what', x, '+', y)
        a = int(input('your answerd: '))
        if a == c:
            print('Well done!')
            print('LEVEL 2'
              '________')
            print('what', x, '**', y)
            a = int(input('your answerd: '))
            e = x ** y
            if a == e:
                print('Great')
                print('FINAL LEVEL'
                  '_______________')
                z = int(input('enter a integer greater than 300: '))
                if z > 300:
                    print('what (' + str(c), '+', str(e) + ')', '*', '(' + str(c), '+', str(e) + ')', '+', z)
                    a = int(input('your answerd: '))
                    k = (c + e) * (c + e) + z
                    if a == k:
                        print("It's fantastic!")
                        print('You win!!!')
                        d += 2
                    else:
                        print('ERROR', '(' + str(c), '+', str(e) + ')', '*', '(' + str(c), '+', str(e) + ')', '+', z, 'is not', a)
                        print('print your answerds again: ')
                else:
                    print('[-]FATAL ERROR')
                    print('Integer less than 300')
                    d += 2
            else:
                print('ERROR', x, '**', y, 'is not', a)
                print('print your answerds again: ')
        else:
            print('ERROR', x, '+', y, 'is not', a)
            print('print your answerds again: ')
    else:
        print('[-] FATAL ERROR')
        print('x or y not(<= 5 and  > 2)')
        d += 2

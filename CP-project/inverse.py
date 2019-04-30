a=input('''what do you want?
1.A-'
2.B/A
''')
def inv():
        if a=='1':
                x=float(input('enter number: '))
                y=1/x
                print('inverse of ',x,'is','1/',x,'=',y)

        elif a=='2':
                x=float(input('enter first number: '))
                y=float(input('enter second number: '))
                z=x/y
                b=y/x
                print('inverse of ',x,'/',y ,'is',y,'/',x,'=',b)

inv()

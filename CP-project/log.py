a=input('''What do you want:
1.common log
2.natural log
''')
if a=='1':
    x=float(input('enter number: '))
    if x<=0:
        print('ERROR')
    else:    
        for i in range(15):
            x=x**0.5
        y=x-1
        log=y/(0.000070271)
        print('log is',log)

elif a=='2':
    x=float(input('enter number: '))
    if x<=0:
        print('ERROR')
    else:
        for i in range(15):
            x=x**0.5
        y=x-1
        log=y/(0.000070271)
        ln=log*2.303
        print('ln is ',ln)

else:
    print("SORRY")
    



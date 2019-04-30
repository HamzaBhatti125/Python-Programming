a=input('''what do you want?
(1).sin
(2).cos
(3).tan
''')
if a=='1':
    x=float(input('enter an angle: '))
    y=(0.0174532)
    sin=(y)*(x)-((x**3)*(y**3)/6)+((x**5)*(y**5)/120)-((x**7)*(y**7)/5040)
    print('sin of ',x,' is ',sin)

elif a=='2':
    x=float(input('enter an angle: '))
    y=(0.0174532)
    sin=(y)*(x)-((x**3)*(y**3)/6)+((x**5)*(y**5)/120)-((x**7)*(y**7)/5040)
    cos=(1-(sin**2))**0.5
    print('cos ',x,' is ',cos)

elif a=='3':
    x=float(input('enter an angle: '))
    y=(0.0174532)
    sin=(y)*(x)-((x**3)*(y**3)/6)+((x**5)*(y**5)/120)-((x**7)*(y**7)/5040)
    cos=(1-(sin**2))**0.5
    tan=sin/cos
    print('tan of ',x,'is',tan)
else:
    print('SORRY')

mat=input('what you want? \n (1).matrix 2x2 \n(2).matrix 3x3 \n')
if mat=='1':
    print(''' |A           B|
 |C           D|=0''')
    w=float(input('enter A: '))
    x=float(input('enter B: '))
    y=float(input('enter C: '))
    z=float(input('enter D: '))

    b=(w*z)-(x*y)
    print('the determinant of 2x2 matrix is ',b)

elif mat=='2':
    print(''' |A           B          C|
 |D           E          F|  =0
 |G           H          I|''')

    a=float(input('enter A '))
    b=float(input('enter B '))
    c=float(input('enter C '))
    d=float(input('enter D '))
    e=float(input('enter E '))
    f=float(input('enter F '))
    g=float(input('enter G '))
    h=float(input('enter H '))
    i=float(input('enter I '))

    x=a*e*i
    y=b*f*g
    z=c*d*h

    p=b*d*i
    q=a*f*h
    r=c*e*g

    ab=(x+y+z)-(p+q+r)
    print('determinant of 3x3 matrix is ',ab)



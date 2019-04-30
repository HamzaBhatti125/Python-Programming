a=input('''what do you want?
1.asin
2.acos
3.atan
'''
        )
if a=='1':
        x=float(input('enter value: '))
        if -1>x>1:
                print("ERROR")
        else:
                a=x+((x)**3/6)+((3*(x)**5)/40)+((15*(x)**7)/336)
                asin=(a*180)/3.1415926
                print(asin)

if a=='2':
        x=float(input('enter value: '))
        if x>1:
                print("ERROR")
        else:
                a=x+((x)**3/6)+((3*(x)**5)/40)+((15*(x)**7)/336)
                asin=(a*180)/3.1415926
                acos=90-asin
                print(acos)

elif a=='3':
        x=float(input('enter value: '))
        if 0<x<1:
                a=x-(x**3/3)+(x**5/5)-(x**7/7)
                atan=(a*180)/3.1415926
                print(atan)
        elif x>=1:
                a=(3.1415926/2)-(1/(x))+(1/(3*(x**3)))-(1/(5*(x**5)))
                atan=(a*180)/3.1415926
                print(atan)
        elif x<=-1:
                a=(-3.1415926/2)-(1/(x))+(1/(3*(x**3)))-(1/(5*(x**5)))
                atan=(a*180)/3.1415926
                print(atan)

                

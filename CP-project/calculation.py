z=1
def calculation(a):
    while z:
        x=input('Enter operator: ')
        if x=='+':
            other_num=float(input('Enter other number '))
            print('sum of ',a,'and',other_num,'is',(a+other_num))
            c=a+other_num
            
        elif x=='-':
            other_num=float(input('Enter other number'))
            print('difference of ',(a),'and',(other_num),'is',(a-other_num))
            c=a-other_num

        elif x=='*':
            other_num=float(input('Enter other number'))
            print('product of ',(a),'and',(other_num),'is',(a*other_num))
            c=a*other_num

        elif x=='/':
            other_num=float(input('Enter other number'))
            print('division of ',(a),'and',(other_num),'is',(a/other_num))
            c=a/other_num

        elif x=='sin':
            y=(0.0174532)
            sin=(y)*(a)-((a**3)*(y**3)/6)+((a**5)*(y**5)/120)-((a**7)*(y**7)/5040)
            print('sin of ',a,' is ',sin)
            c=sin

        elif x=='asin':
            if -1>a>1:
                print("ERROR")
            else:
                b=a+((a)**3/6)+((3*(a)**5)/40)+((15*(a)**7)/336)
                asin=(b*180)/3.1415926
                print('asin is',asin)
            c=asin
            
        elif x=='cos':
            y=(0.0174532)
            sin=(y)*(a)-((a**3)*(y**3)/6)+((a**5)*(y**5)/120)-((a**7)*(y**7)/5040)
            cos=(1-(sin**2))**0.5
            print('cos ',a,' is ',cos)
            c=cos

        elif x=='acos':
            if -1>a>1:
                print("ERROR")
            else:
                b=a+((a)**3/6)+((3*(a)**5)/40)+((15*(a)**7)/336)
                asin=(b*180)/3.1415926
                acos=90-asin
                print('acos is ',acos)
            c=acos

        elif x=='tan':
            y=(0.0174532)
            sin=(y)*(a)-((a**3)*(y**3)/6)+((a**5)*(y**5)/120)-((a**7)*(y**7)/5040)
            cos=(1-(sin**2))**0.5
            tan=(sin)/(cos)
            print('tan of ',a,' is ',tan)
            c=tan

        elif x=='atan':
            if 0<a<1:
                b=a-(a**3/3)+(a**5/5)-(a**7/7)
                atan=(b*180)/3.1415926
                print('atan is ',atan)
            elif a>=1:
                b=(3.1415926/2)-(1/(a))+(1/(3*(a**3)))-(1/(5*(a**5)))
                atan=(b*180)/3.1415926
                print('atan is ',atan)
            elif a<=-1:
                b=(-3.1415926/2)-(1/(a))+(1/(3*(a**3)))-(1/(5*(a**5)))
                atan=(b*180)/3.1415926
                print('atan is ',atan)
            c=atan

        elif x=='sqr':
            print('square of ',(a),'is ',(a**2))
            c=a**2

        elif x=='power':
            p=int(input('enter power: '))
            print(p,'th power of ',(a),'is ',(a**p))
            c=a**p

        elif x=='root':
            r=int(input('enter root '))
            print(r,'th root of ',(a),'is',(a**(1/r)))
            c=a**(1/r)

        elif x=='ln':
            if a<=0:
                print('ERROR')
            else:
                for i in range(15):
                    a=a**0.5
                y=a-1
                log=y/(0.000070271)
                ln=log*2.303
                print('ln is ',ln)
            c=ln

        elif x=='log10':
            if a<=0:
                print('ERROR')
            else:    
                for i in range(15):
                    a=a**0.5
                y=a-1
                log=y/(0.000070271)
                print('log is',log)
            c=log

        elif x=='!':
            b=int(a)
            fac=1
            if b<0:
                print('no Factorial')
            elif b==0:
                print('Factorial is 1')
            else:
                for i in range(1,b+1):
                    fac=fac*i
            print('factorial of ',(b),' is ',(fac))
            c=fac
        
        else:
            print("no function exist of this type")
            break
        a=c
first_num=float(input('enter first number: '))
calculation(first_num)
            
            
                  

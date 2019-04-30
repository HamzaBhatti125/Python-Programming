while True:
    print('\t*** Hello i am your scientific Calculator welcome***')
    x=input("""What do you want to do?
(1).conversions            (2).quadratic equation      (3).root of number
(4).power of number        (5).trigonomerty            (6).inverse trigonometry
(7).log                    (8).factorial               (9).percentage
(10).hyperbolic functions  (11).nPr & nCR              (12).inverse of variable
(13).antilog               (14).Determinant of matrix  (15).exponential
(16).calculation

""")
    if x=='1':
        cn=input('what conversion you want \n 1.angle \n 2.temperature \n 3.length \n')
        if cn=='1':
            import angle
            continue
        elif cn=='2':
            import temperature
        elif cn=='3':
            import length
        else:
            print('sorry')
    elif x=='2':
        import quadratic
        continue
        
    elif x=='3':
        rt=input('what you want \n 1.sqr root \n 2.cube root \n 3.nth root \n')
        if rt=='1':
            import squareroot
        elif rt=='2':
            import cuberoot
        elif rt=='3':
            import nthroot
        else:
            print('sorry')
    
    elif x=='4':
        pwr=input('what you want \n 1.square \n 2.cube \n 3.nth power \n')
        if pwr=='1':
            import square
        elif pwr=='2':
            import cube
        elif pwr=='3':
            import nthpower
        else:
            print('Sorry')
   
    elif x=='5':
        import trigonometry

    elif x=='6':
        import inversetrigonometry

    elif x=='7':
        import log

    elif x=='8':
        import factorial

    elif x=='9':
        import percentage
            
    elif x=='10':
        import hyperbolic
    
    elif x=='11':
        abc=input('What do you want?: \n(1).nPr \n(2).nCr \n')
        if abc=='1':
            import permutation
        elif abc=='2':
            import combination
       
    elif x=='12':
        import inverse

    elif x=='13':
        import antilog

    elif x=='14':
        import determinant

    elif x=='15':
        import exponential
    
    elif x=='16':
        import calculation

   
        
    else:
        print("ERROR")
        break
        

    con=input('do you want to continue? ')
    if con=='y':
        continue
    else:
        print('Thankyou !')
        break
    
        

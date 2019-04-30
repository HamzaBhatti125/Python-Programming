B=1
while B:
    A=int(input("ENTER \n 1 TO CONVERT ANGLE IN RADIANS \n 2 TO CONVERT ANGLE IN DEGRESS \n"))
    if A==1:
        S=float(input("ANGLE IN RADIANS:"))
        P=3.14
        Y=180
        U=Y/P
        Q=U*S
        print(S,"RADIANS IS EQUAL TO",Q,"DEGREES")
        break
    
    elif A==2:
        S=float(input("ANGLE IN DEGREES:"))
        P=3.14
        Y=180
        U=P/Y
        Z=U*S
        print(S,"DEGREES IS EQUAL TO",Z,"RADIANS")
        break
    
    else:
        break
   

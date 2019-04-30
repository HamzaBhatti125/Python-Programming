X=1
while X:
    A=int(input("PRESS \n 1 TO CONVERT LENGTH INTO CENTIMETER \n 2 TO CONVERT LENGTH INTO METERS"))
    if A==1:
        B=float(input("LENGTH IN METERS"))
        C=B*100
        print(B,"METERS IS EQUAL TO",C,"CENTIMETERS")
        break
    elif A==2:
        B=float(input("LENGTH IN CENTIMETERS"))
        C=B/100
        print(B,"CENTIMETERS IS EQUAL TO",C,"METERS")
        break

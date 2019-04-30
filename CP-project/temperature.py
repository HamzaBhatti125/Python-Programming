x=1
while x:
    C=int(input("ENTER \n 1 TO CONVERT TEMPERATURE INTO FAHRENHEIT \n 2 TO CONVERT TEMPERATURE IN CELSIUS \n"))
    if C==1:
        A=float(input("TEMPERATURE IN FAHRENHEIT:"))
        B=(A-32)*0.556
        print(A,"degree FAHRENHEIT IS EQUAL TO",B,"degree CELSIUS")
        break
    elif C==2:
        A=float(input("TEMPERATURE IN CELSIUS:"))
        B=(A)*1.8+32
        print(A,"degree CELSIUS IS EQUAL TO",B,"degree FAHRENHIET")
        break
    else:
        break

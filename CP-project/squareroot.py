square_root = 1
while square_root:
    square_root=float(input("enter the number "))
    if square_root > 0:
        b = square_root ** 0.5
        print("Answer of",square_root,'**','1/2','is',b)
        break
    elif square_root < 0:
        print("please enter the positve number")
        break
    else:
        print('ERROR')
        break
        

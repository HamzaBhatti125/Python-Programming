x=input('what do you want \n 1.sinh \n 2.cosh \n 3.tanh \n')
if x=='1':
    z=float(input('enter angle: '))
    sinh=((2.7182818)**z - (2.7182818)**(-z))/2
    print('sinh of ',z,'is ',sinh)
elif x=='2':
    z=float(input('enter angle: '))
    sinh=((2.7182818)**z - (2.7182818)**(-z))/2
    cosh=(1+(sinh)**2)**0.5
    print('cosh of ',z,'is ',cosh)

elif x=='3':
    z=float(input('enter angle: '))
    sinh=((2.7182818)**z - (2.7182818)**(-z))/2
    cosh=(1+(sinh)**2)**0.5
    tanh=(sinh)/(cosh)
    print('tanh of ',z,'is ',tanh)
    
else:
    print("SORRY")

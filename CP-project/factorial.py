x=int(input('enter a number: '))
y=1
if x<0:
    print('Please Enter positive number ')
elif x==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,x+1):
        y=y*i
    print('factorial of ',x,' is ',y)

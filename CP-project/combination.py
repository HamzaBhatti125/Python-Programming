def fact(x):
        if x==1:
                return 1
        else:
                return x * fact(x-1)

n=int(input('enter first number: '))
r=int(input('enter second number: '))

def com(n,r):
        if n<0 or r<0:
                print('please enter positive number')
        else:
                combination=(fact(n))/(fact(n-r)*fact(r))
                print('combination is ',combination)

com(n,r)

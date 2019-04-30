def fact(x):
        if x==1:
                return 1
        else:
                return x * fact(x-1)


n=int(input('enter first number: '))
r=int(input('enter second number: '))

def per(n,r):
        if n<0 or r<0:
                print('please enter positive number')
        else:
                permutation=fact(n)/fact(n-r)
                print('permutation is ',permutation)

per(n,r)

a`nth_root=1
while nth_root:
    nth_root=int(input("Enter your root number: "))
    value=float(input("Enter your number: "))
    if value > 0:
        answer_of_root=value**(1/nth_root)
        print("Answer of your root is",answer_of_root)

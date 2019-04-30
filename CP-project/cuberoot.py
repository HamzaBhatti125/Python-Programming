cube_root=float(input("Enter your number for cube root "))
if cube_root > 0:
    ans_root=cube_root**(1/3)
    print("Cube root of ",cube_root,"is",ans_root)
elif cube_root < 0:
    print("Please enter the positve number")
else:
    print("ERROR")
        

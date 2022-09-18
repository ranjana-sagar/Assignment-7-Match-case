x=(input(""" Choose the option:
a. Check whether a given set of three numbers are lengths of an isosceles Triangle or not.
b. Check whether a given set of three numbers are lengths of an sides of a right angled triangle or not.
c. Check whether a given set of three numbers are equilateral triangle or not.
d. Exit."""))
match x:
    case 'a':
        a1=eval(input("Enter the first length of triangle's side:"))
        b1=eval(input("Enter the second length of triangle's side:"))
        c1=eval(input("Enter the third lengths of triangle's side:"))
        if a1==b1 or b1==c1 or c1==a1:
            print('This is a Isosceles triangle')
        else:
            print('This is not isosceles triangle')
    case 'b':
        a1=eval(input("Enter the first length of triangle's side:"))
        b1=eval(input("Enter the second length of triangle's side:"))
        c1=eval(input("Enter the third lengths of triangle's side:"))
        if a1>b1 and a1>c1:
            if a1*a1==b1*b1+c1*c1:
                print("This is a right angle triangle")
            else:
                print("this is not right angle triangle")
        elif b1>c1:
            if b1*b1==a1*a1+c1*c1:
                print("This is a right angle triangle")
            else:
                print("this is not right angle triangle")
        else:
            if c1*c1==a1*a1+b1*b1:
                print("This is a right angle triangle")
            else:
                print("this is not right angle triangle")
    case 'c':
        a1=eval(input("Enter the first length of triangle's side:"))
        b1=eval(input("Enter the second length of triangle's side:"))
        c1=eval(input("Enter the third lengths of triangle's side:"))
        if a1==b1==c1:
            print("This is a equilateral triangle")
        else:
            print("This is a not equilateral triangle")
    case 'd':
        exit()
        
         
            
                
        

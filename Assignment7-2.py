a=input("What do you want to perform?,Addition,Subtraction,multiply,division:")
x=eval(input("Enter first number:"))
y=eval(input("Enter second number:"))
match a:
    case "addition":
        print("Sum of",x,',',y,'is:',x+y)
    case "subtraction":
        print("subtraction of",x,',',y,'is:',x-y)
    case 'multiply':
        print("multiply of",x,',',y,'is:',x*y)
    case 'division':
        print("division of",x,',',y,'is:',x/y)
    case _:
        print("This operation is not in menu")

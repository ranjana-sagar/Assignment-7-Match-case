x=eval(input("Enter a number:"))
if x>0:
    x=1
elif x==0:
    x=2
else:
    x=3
match x:
    case 1:
        print("positive number")
    case 2:
        print("zero")
    case 3:
        print("Negative number")

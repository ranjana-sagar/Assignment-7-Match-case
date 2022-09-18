a=int(input("Enter your age:"))
if 0<a<=10:
    a='below 10'
elif 10<a<=20:
    a='below 20'
elif 20<a<=40:
    a='below 40'
elif 40<a<60:
    a='below 60'
elif 60<=a:
    a='above or equal 60'
match a:
    case 'below 10':
        print("kid")
    case 'below 20':
        print("Teen")
    case 'below 40':
        print("Young")
    case 'below 60':
        print("Experienced")
    case 'above or equal 60':
        print("Senior citizen")
    case _:
        print("Invalid age")

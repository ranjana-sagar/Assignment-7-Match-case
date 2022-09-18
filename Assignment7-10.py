x=input("Enter your favourite colour:")
if 'yellow' in x:
    x='yellow'
elif 'blue' in x:
    x='blue'
elif 'orange' in x:
    x='orange'
elif 'white' in x:
    x='white'
elif 'black' in x:
    x='black'
elif 'red' in x:
    x='red'
match x:
    case 'yellow':
        print("Monday")
    case 'blue':
        print("Tuesday")
    case 'orange':
        print("Wednesday")
    case 'white':
        print("Thurusday")
    case 'black':
        print("Friday")
    case 'red':
        print("Saturday")
    case _:
        print("Sunday")

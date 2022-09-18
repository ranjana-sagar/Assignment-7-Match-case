x=int(input("Enter an year:"))
if x%100!=0:
    if x%4==0:
        x='a'
    else:
        x='c'
elif x%100==0:
    if x%400==0:
        x='b'
    else:
        x='d'
match x:
    case 'a':
        print("Non century leap year")
    case 'b':
        print("Century year leap year")
    case 'c':
        print("Non century non leap year")
    case 'd':
        print("century non leap year")

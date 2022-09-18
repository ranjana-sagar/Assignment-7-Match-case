x=int(input("Enter a number:"))
if x>0:
    y='even'if x%2==0 else'positive odd'
else:
    if x%2!=0:
        y='negative odd'
    else:
        y=""
match y:
    case 'even':
        print("Saurabh Shukla")
    case 'negative odd':
        print("Prateek Jain")
    case 'positive odd':
        print("Aaditya Choudhary")
    case _:
        print("This is Negative even number")

x=input("Enter the first string:")
y=input("Enter the second string:")
if x==y:
    a=1
elif x>y:
    a=2
else:
    a=3
match a:
    case 1:
        print("Given strings are similar to each other")
    case 2:
        print("First string comes after the second string")
    case 3:
        print("First string comes before the second string")

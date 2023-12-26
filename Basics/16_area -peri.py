def area():
    l = int(input("\nEnter the length: "))
    b = int(input("Enter the width: "))
    print("\nArea =",l*b)

def peri():
    l = int(input("\nEnter the length: "))
    b = int(input("Enter the width: "))
    return 2(l+b)

def vol(l,b,h):
    return l*b*h

def sur_area():
    l = int(input("\nEnter the length: "))
    b = int(input("Enter the width: "))
    h = int(input("Enter the height: "))
    print("\nSurface area =",(2*(l*b))+(2*(l*h)+(2*(b*h))))

def decider(a):
    if a == "y":
        return 1
    else :
        return 0

def main():
    c = 1
    print("Hello !\nWhat can we help you with\n\n1.Area of regular quad\n2.Perimeter of regular quad\n3.Volume \n4.Surface Area")
    while c :
        o = int(input("\nEnter the number of the operation you want to perform : "))
        match o:
            case 1:
                area()
            case 2:
                print("\nPerimater =",peri())
            case 3:
                l = int(input("\nEnter the length: "))
                b = int(input("Enter the width: "))
                h = int(input("Enter the height: "))
                print("\nVolume =",vol(l,b,h))
            case 4:
                sur_area()
        dec = input("Do you want to continue(y/n): ")
        c = decider(dec)

    
main()
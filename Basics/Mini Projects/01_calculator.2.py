# defining main and asking the task to be done
def main():
    print("\nWelcome !\nThis is a mini Calculator :)\n")
    a = int(input("Enter the first number : "))
    choice = input("Enter the operator \n '+'  '-'  '*'  '/'  '%'  '^' : ")
    b = int(input("Enter the second number : "))

    match choice :
        case '+':
            print(f"\nThe sum of {a} + {b} = {a + b} .")
        case '-':
            print(f"\nThe difference of {a} - {b} = {a + b} .")
        case '*':
            print(f"\nThe product of {a} * {b} = {a * b} .")
        case '/':
            print(f"\nThe quotient of {a} / {b} = {a / b} .")
        case '%':
            print(f"\nThe remainder of {a} / {b} = {a % b} .")
        case '^':
            print(f"\nThe value of {a} raised to power {b} = {pow(a ,b)} .")
        case _:
            print("Unknown Operator .")    
    print("\nThank You !!")
    
# calling the main function 
main()
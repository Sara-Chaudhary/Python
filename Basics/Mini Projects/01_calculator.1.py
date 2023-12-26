# defining main and asking the task to be done
def main():
    print("\nWelcome !\nThis is a mini Calculator :) \n\nWith this you can :\n1.Add two numbers \t\t2.Subtract two numbers \n3.Multiply two numbers \t\t4.Divide numbers")
    print("5.Get the remainder \t\t6.Raise a number to power \n ")
    choice = input("You Wish to :")
    match choice :
        case '1':
            add()
        case '2':
            sub()
        case '3':
            mult()
        case '4':
            div()
        case '5':
            mod()
        case '6':
            power()
    print("\nThank You !!")

# defining all the functions that can be done 
def add(): 
    a = int(input("\nEnter the first number : "))
    b = int(input("Enter the second number : "))  
    print(f"The sum of {a} + {b} is : {a + b} .")

def sub():
    a = int(input("\nEnter the first number : "))
    b = int(input("Enter the second number : "))
    print(f"The difference of {a} - {b} is : {a - b} .")

def mult():
    a = int(input("\nEnter the first number : "))
    b = int(input("Enter the second number : "))
    print(f"The product of {a} * {b} is : {a * b} .")

def div():
    a = int(input("\nEnter the divident : "))
    b = int(input("Enter the divisor : "))
    print(f"The quotient of {a} / {b} is : {a / b} .")

def mod():
    a = int(input("\nEnter the first number : "))
    b = int(input("Enter the second number : "))
    print(f"The remainder of {a} / {b} is : {a % b} .")

def power():
    a = int(input("\nEnter the number : "))
    b = int(input("Enter the power you want to raise the number to : "))
    print(f"The value of {a} to power of {b} is : {pow(a , b)} .")
    
# calling the main function 
main()
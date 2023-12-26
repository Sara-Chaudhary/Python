def main():
    x = True
    while x:
        a = int(input("\nEnter a number : "))
        check(a)
        b = input("\nDo you want to check another number (y or n) : ")
        if(b == 'n'):
            x = False
    print("\nThank You !!")

def check(n):
    if n >= 0 :
        print(f"{n} is a positive integer .")  
    else:
        print(f"{n} is a negative integer .")
                                                                                                                                                                    
main()
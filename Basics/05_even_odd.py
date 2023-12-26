# defining the main function
def main():
    x = int(input("\nEnter a number : "))
    if even_odd(x):
        print(f"The number {x} is even .\n")
    else :
        print(f"The number {x} is odd .\n")

#checking if a number is odd or even
def even_odd(n):
    if n % 2 == 0 :
        return True
    else :
        return False
    
    # OR
    # we can compact the above function like --->
    # { return True if n % 2 == 0 else False  }

# calling the main function
main()
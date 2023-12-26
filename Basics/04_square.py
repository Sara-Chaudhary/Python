# defining a main function to execute the task 
def main():
    x = int(input("\nEnter a number : "))
    print(f"{x} squared is: {square(x)} \n")

# defining a function to return square of the given number 
def square(n):    
    return n*n 

# calling main 
main()
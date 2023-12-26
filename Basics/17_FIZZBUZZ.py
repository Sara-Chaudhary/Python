'''
A programme that 
Prints 'FizzBuzz' if the number is divisible by 3 and 5.
Prints 'Fizz' if the number is only divisible by 3.
Prints 'Buzz' if the number is only divisible by 5.
Prints the number if the number is neither divisible by 3 nor 5.
'''
def fizzbuzz(n):
    for i in range(1,n):
        if (i % 3 == 0) & (i%5 == 0):
            print("FizzBuzz",end=" ")
        elif i % 3 == 0 :
            print("Fizz",end=" ")
        elif i % 5 == 0 :
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

def main():
    a = int (input("Enter the limit number : "))
    fizzbuzz(a)

main()
#  program to counting down number
def count_down(n):
    if n == 0:
        return
    print(n , end=" ")
    count_down(n-1)

def count_up(n):
    if n == 0:
        return
    count_up(n-1)
    print(n , end=" ")

def checker(c):
    if c == "y":
        main()

def main():
    a = int(input("Enter a number: "))
    count_down(a)
    print()
    count_up(a)
    choice = input("\nDo you want to continue (y/n): ")
    checker(choice)

main()
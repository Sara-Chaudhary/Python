# programme to give the factorial of number

def main():
    n = int(input("\nEnter a number : "))
    fac(n)

def fac(n):
    pro = 1
    for i in range(n):
        pro = pro * (i+1)
    print(f"The factorial of {n} = {pro} .\n")

main()
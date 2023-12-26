def power(base,exponent):
    if exponent == 0:
        return 1
    return base * power(base*(exponent-1))

def main():
    a = int(input("Enter the base value: "))
    b = int(input("Enter the exponent: "))
    print(power(a,b))

main()

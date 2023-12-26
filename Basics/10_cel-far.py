def cel_far(c):
    return((c*9/5)+32)

def main():
    cel = int(input("Enter temp in celsius: "))
    print("Temp in Farenheit =",cel_far(cel))

main()
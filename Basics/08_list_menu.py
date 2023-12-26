l = [i *(i+1) for i in range(6) ] # initiating a list so that every number is product of itself and its next term.
print("Hello :)\nWelcome to the List Menu.\n\nYou can :")

# starting a infinte loop 
while True:
    print("1.Print the list\t 2.Add numbers to the list\n3.Sort list(Ascending)   4.Sort list(Descending)\n5.Check the presence of a number in the list\n6.Count the occurences of a element\n")
    c = int(input("Your choice : "))
    match c:
        case 1: # printing the list
            print(f"List : {l}")

        case 2: # adding  number to the number
            n =int (input("How many numbers do you want to add to the list : ")) 
            for _ in range(n):
                x = int(input(f"Enter the number {_+1}: "))
                index = int(input(f"Enter the index for number {_+1}: "))
                l.insert(index , x)
            print(f"New list : {l}")

        case 3: # sorting the list in ascending order 
            l.sort()
            print(f"Sorted list (Ascending order): {l}")

        case 4: # sorting the list in descending order
            l.sort(reverse=True)
            print(f"Sorted list (Descending order): {l} \n") 

        case 5: # printing the first occurence index of a number given by user
            x = int(input("Enter the number you want to check : "))
            if x in l:
                print(f"Yes ,{x} is present in the list . First occur at {l.index(x)} ")
            else :
                print("No , not present ")

        case 6: # counting the occurence of a number given by user
            x = int(input("You want the occurences of which number : "))  
            print(l.count(x))
            
    # proving option to get out of the loop
    choice = input("\nWant to do anything else (yes/no): ")
    if choice == 'no':
        print("Thank you for using this .\n")
        break      
     


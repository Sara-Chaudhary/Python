def main():
    print('''\nHello\nWelcome to the Matchstick game .\nIt's very easy\n\nThere are 21 matchsticks in total .\nAt a time you can pick out either 1 ,2 ,3 or 4 matchsticks.\nAfter your chance computer choose .\nAnd game continues till no matchstick is left.\nPerson to choose the last matchstick will lose.''')
    choice = input("\nAre you ready to play : ")
    
    while choice == 'yes':
        total = 21
        while total != 1:
            print(f"\nMatchsticks : {total}")
            user = int(input("Your move : "))
            user1 = check(user)
            print(f"Computer's move : {5 - user1} ")
            total = total - 5
        print("only 1 matchstick left\nYou Lose")
        choice = input("Want to try again : ")

# this function is to check if the value entered by the user is valid or not
def check(num):
    if num <0 or num>5:
        print("Invalid move.")
        a = int(input("Pick again: "))
        num = check(a)
        return()
    else :
        return(num)

main()



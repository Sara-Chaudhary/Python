# asking user for name
name = input("\nEnter your full name: ")

# strip the space , capatilize
name = name.strip().title()

# Spltting the name
first , last = name.split(" ")

print("Hello "+ first + " !!\n")
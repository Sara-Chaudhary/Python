import textwrap

# using a fuction 
def wrap_text(str , width):
    return textwrap.fill(str , width)

a = input("Enter the string: ")
n = int(input("Enter the width of substring: "))
print(wrap_text(a,n))

# without function
# a = input("Enter the string: ")
# n = int(input("Enter the width of substring: "))
# print(textwrap.fill(a,n))
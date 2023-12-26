def clr(a,b):
    c= a+b
    if c % 2 == 0:
        return ("White")
    else :
        return("Black")

c=1
while c:      
    n = int(input("Enter the row : "))
    m = int(input("Enter the column: "))
    if (m <= 7) & (n <=7):
        print("The block [",n ,",",m,"] is :",clr(n,m)) 
        break
    else :
        print("\bInvalid response.\nBlock can be only till 7.\n")    
   

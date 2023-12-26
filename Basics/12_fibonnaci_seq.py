def fib_seq(n):
   if n <= 1:
      return n
   return fib_seq(n-1)+ fib_seq(n-2)

def main():
   a = int(input("enter a number : "))
   result = [fib_seq(i) for i in range(a)]
   print(result)

main()

                                
                     
import math

def findDivisors(n):
   # Initialize an empty
   # list to store the divisors
   divisors = [] 

   # Iterate up to the square
   # root of n to find divisors
   # Calculate the square root of n
   sqrtN = int(math.sqrt(n)) 
   
   # Loop from 1 to the
   # square root of n
   for i in range(1, sqrtN + 1): 
      # Check if i divides n
      # without leaving a remainder
      if n % i == 0: 
         # Add divisor i to the list
         divisors.append(i) 
         print(f"{i}x{n//i}")

         # Add the counterpart divisor
         # if it's different from i
         if i != n // i:
               # Add the counterpart
               # divisor to the list
               divisors.append(n // i) 
   
   # Return the list of divisors
   return divisors 

if __name__ == "__main__":
   number = 27
   divisors = findDivisors(number)

   print("Divisors of", number, "are:", end=" ")
   for divisor in divisors:
      print(divisor, end=" ")
   print()                      
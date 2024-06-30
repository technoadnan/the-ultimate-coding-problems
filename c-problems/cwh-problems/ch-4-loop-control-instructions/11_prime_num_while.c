#include <stdio.h>

int main(int argc, char const *argv[])
{
   int num = 3, prime = 1; // Assume it's prime until proven otherwise
   int i = 2;
   while (i<num)
   {
      if (num % i == 0)
      {
         prime = 0; // Set prime to 0 if a factor is found
         break;     // No need to continue checking
      }
      i++;
   }

   if (num <= 1)
      prime = 0; // 1 is not considered a prime number

   if (prime == 1 || prime == 2)
   {
      printf("%d is prime\n", num);
   }
   else
   {
      printf("%d is not prime\n", num);
   }

   return 0;
}

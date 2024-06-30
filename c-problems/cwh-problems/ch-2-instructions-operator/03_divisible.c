#include <stdio.h>

int main(int argc, char const *argv[])
{
   int num;
   printf("Write a number: ");
   scanf("%d", &num);

   if (num % 2 == 0)
   {
      printf("The number is divisible ");
   } else {
      printf("The number is not divisible");
   }
   return 0;
}

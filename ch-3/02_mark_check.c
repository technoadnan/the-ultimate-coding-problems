#include <stdio.h>

int main(int argc, char const *argv[])
{
   float sub1, sub2, sub3;

   printf("Enter number for sub1: ");
   scanf("%f", &sub1);
   printf("Enter number for sub2: ");
   scanf("%f", &sub2);
   printf("Enter number for sub3: ");
   scanf("%f", &sub3);

   float result_total = (sub1 + sub2 + sub3) / 3;
   if (sub1 >= 33 && sub2 >= 33 && sub3 >= 33 && result_total >= 40)
   {
      printf("PASSED!!!");
   } 
   else 
   {
      printf("FAILED!!!");
   }

   return 0;
}

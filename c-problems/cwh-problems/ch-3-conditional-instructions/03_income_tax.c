#include <stdio.h>

int main(int argc, char const *argv[])
{
   int income;
   printf("Income: ");
   scanf("%d", &income);

   if (income <= 250000) 
   {
      printf("No tax");
   }
   else if (income > 250000 && income <= 500000)
   {
      printf("%d", (5*income)/100 );
   }
   else if (income > 500000 && income <= 1000000)
   {
      printf("%d", (20*income)/100 );
   }
   else if (income > 1000000)
   {
      printf("%d", (30*income)/100);
   }
   
}

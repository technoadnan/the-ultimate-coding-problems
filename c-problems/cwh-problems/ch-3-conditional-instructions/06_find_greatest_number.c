#include <stdio.h>
#include <ctype.h>
int main(int argc, char const *argv[])
{
   int num1, num2, num3, num4;
   printf("Enter the first number: ");
   scanf("%d", &num1);
   printf("Enter the first number: ");
   scanf("%d", &num2);
   printf("Enter the first number: ");
   scanf("%d", &num3);
   printf("Enter the first number: ");
   scanf("%d", &num4);
   

   // 10, 25, 8, and 18

   int highest = 0;
   if (num1 > highest)
   {
      highest = num1;
      if (num2 > highest)
      {
         highest = num2;
         if (num3 > highest)
         {
            highest = num3;
            if (num4 > highest)
            {
               highest = num4;
            }
         }
      }
   }
   
   printf("%d is highest among four", highest);

   return 0;
}

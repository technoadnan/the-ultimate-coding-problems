#include <stdio.h>

int main(int argc, char const *argv[])
{
   int num;
   printf("Enter the number: ");
   scanf("%d", &num);

   for (int i = 10; i >= 0; i--)
   {
      printf("%d * %d = %d\n", num, i, (num * i));
   }

   return 0;
}
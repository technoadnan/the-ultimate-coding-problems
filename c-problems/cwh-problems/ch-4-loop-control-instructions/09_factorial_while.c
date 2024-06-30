#include <stdio.h>

int main(int argc, char const *argv[]) 
{
   int num = 5;
   int result = 1;
   while (num > 1)
   {
      result = result * num * (num - 1);
      num -= 2;
   }
   printf("%d\n",result);
   return 0;
}
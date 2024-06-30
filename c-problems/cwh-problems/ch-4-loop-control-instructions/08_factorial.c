#include <stdio.h>

int main(int argc, char const *argv[]) 
{
   int num = 5;
   int result = 1;
   for (int i = num; i > 1; i-=2)
   {
      result = result * i * (i - 1);
   }
   printf("%d\n",result);
   
   return 0;
}
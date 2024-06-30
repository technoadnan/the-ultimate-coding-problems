#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{
   int *ptr;
   ptr = (int *)calloc(5, sizeof(int));
   for (int i = 0; i < 5; i++)
   {
      int num;
      scanf("%d", &num);
      ptr[i] = num;
   }

   for (int i = 0; i < 5; i++)
   {
      printf("%d\n", ptr[i]);
   }

   ptr = realloc(ptr, 10 * sizeof(int));
   for (int i = 0; i < 10; i++)
   {
      scanf("%d", &ptr[i]);
   }
   for (int i = 0; i < 10; i++)
   {
      printf("%d", ptr[i]);
   }

   return 0;
}
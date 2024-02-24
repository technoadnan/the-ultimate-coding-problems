#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[]) {
   int *ptr;
   ptr = (int*) malloc(6 * sizeof(int));
   for (int i = 0; i < 6; i++)
   {
      int num;
      scanf("%d",&num);
      ptr[i] = num;
   }
   for (int i = 0; i < 6; i++)
   {
      printf("%d\n", ptr[i]);
   }

   return 0;
}
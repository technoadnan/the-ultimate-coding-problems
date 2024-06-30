#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {

   int *ptr;
   ptr = malloc(10 * sizeof(int));

   int i = 1;
   for (i = 1; i < 11; i++)
   {
      ptr[i] = i * 7;
   }
   ptr = realloc(ptr, sizeof(int) * 5);
   for (int i = 0; i < 16; i++)
   {
      ptr[i] = i * 7;
   }
   
   for (i = 1; i < 16; i++)
   {
      printf("7 X %d = %d\n", i, ptr[i]);
   }  
   free(ptr);


   return 0;
}
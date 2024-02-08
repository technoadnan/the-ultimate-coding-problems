#include <stdio.h>

int main(int argc, char const *argv[]) {
   
   char star = '*';
   int n = 1;
   for (int i = 0; i < 3; i++)
   {
      for (int i = 0; i < n; i++)
      {
         printf("%c", star);
      }
      printf("\n");
      n = n + 2;
   }
   
   return 0;
}
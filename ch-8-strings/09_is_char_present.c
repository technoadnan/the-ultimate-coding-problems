#include <stdio.h>


int is_present(char arr[], char c);

int main(int argc, char const *argv[]) {
   char str[] = "err"; // 0
   printf("%d", is_present(str, 'a'));
   
   return 0;
}

int is_present(char arr[], char c)
{
   for (int i = 0; arr[i] != '\0'; i++)
   {
      if (arr[i] == c)
      {
         return 1; // yes 
      }
   }
   return 0; // no
   
}
#include <stdio.h>
#include <string.h>

char count(char arr[], char c);

int main(int argc, char const *argv[]) {
   char str[] = "adnan"; //2 
   int a = count(str, 'a');
   printf("%d", a);
   
   return 0;
}

char count(char arr[], char c)
{
   int n = 0;
   for (int i = 0; i < strlen(arr); i++)
   {
      if (arr[i] == c)
      {
         n++;
      }
   }
   return n;
}
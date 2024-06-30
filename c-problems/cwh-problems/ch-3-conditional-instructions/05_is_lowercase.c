#include <stdio.h>
#include <ctype.h>

int main(int argc, char const *argv[])
{
   char character;
   printf("Enter the character: ");
   scanf("%c", &character);
   
   if (islower(character))
   {
      printf("The char is a lowercase letter ");
   }
   else
   {
      printf("The char is not a lowercase letter");
   }
   
   return 0;
}

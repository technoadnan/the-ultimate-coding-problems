#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[]) {
   char input1[20], input2[20], c;
   int i=0;

   printf("Enter the value of first string\n");
   scanf("%s", &input1);
   printf("Enter the value of second string character by character\n");

   while (c!='\n')
   {
      fflush(stdin);
      scanf("%c", &c);
      input2[i] = c;
      i++;
   }
   input2[i-1] = '\0';

   printf("%d", strcmp(input1, input2));

    
   return 0;
}
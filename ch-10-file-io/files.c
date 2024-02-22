#include <stdio.h>

int main(int argc, char const *argv[]) {
   FILE *ptr;
   ptr = fopen("sample.txt", "r");

   while (1)
   {
      char ch = fgetc(ptr);
      printf("%c",ch);
      if(ch == EOF)
      {
         break;
      }
   }

   if (ptr == NULL)
   {
      printf("This file does not exist\n");
   }
   else
   {
      char str[30];
      fscanf(ptr,"%s",&str);
      printf("%s",str); // Hello

      char c1;
      fscanf(ptr, "%c", &c1);
      printf("%c", c1); // space
      char c2;
      fscanf(ptr, "%c", &c2);
      printf("%c", c2); // t
   }


   FILE *ptrread;
   ptrread = fopen("generated.txt", "w");
   fprintf(ptrread, "Hello world ");
   int num1 = 100;
   fprintf(ptrread, "%d", num1);
   fclose(ptrread);


   // FILE *ptr_f_get_put;
   // ptr_f_get_put = fopen("upt.txt","w");

   return 0;
}
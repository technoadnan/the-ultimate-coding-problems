#include <stdio.h>

int main(int argc, char const *argv[]) {
   FILE *ptr;
   ptr = fopen("01_read_int.txt","r");

   while (1)
   {
      int num = fgetc(ptr);
      // char ch = fgetc(ptr);
      printf("%c",num); // we have to use %c because it's treating numbers as characeters now 
      if (num == EOF)
      {
         break;
      }
   }

   fclose(ptr);
   printf("\n");

   // another way to do
   int a,b,c;
   FILE *ptr1;
   ptr1 = fopen("01_read_int.txt","r");
   fscanf(ptr1, "%d %d %d",&a,&b,&c);
   printf("%d %d %d",a,b,c);
   return 0;
}
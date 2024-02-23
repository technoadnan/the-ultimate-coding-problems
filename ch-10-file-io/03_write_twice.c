#include <stdio.h>

int main(int argc, char const *argv[]) {
   FILE *fptr;
   fptr = fopen("03_write_twice_read.txt","r");
   char arr[100];

   // read the file by character by character
   int i=0;
   while (1)
   {
      char ch = fgetc(fptr);
      if (ch == EOF)
      {
         break;
      }
      arr[i] = ch;
      i++;
   }

   // using same ptr's free space to write double
   int j=0,k=i; // k=i so that we know when to stop
   while (1)
   {
      arr[i] = arr[j];
      i++,j++;
      if (j==k)
      {
         arr[i] = '\0';
         break;
      }   
   } 


   // write in the new file 
   fptr = fopen("03_write_twice_upt.txt","w");
   fprintf(fptr,"%s" ,arr);
   fclose(fptr);

   
   return 0;
}
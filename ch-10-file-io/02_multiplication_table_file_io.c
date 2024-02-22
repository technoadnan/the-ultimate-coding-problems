#include <stdio.h>

int main(int argc, char const *argv[]) {
   int num; // 5
   scanf("%d",&num);

   FILE *ptr;
   ptr = fopen("02_multiplication_table_file_io.txt","w");
   for (int i = 1; i <= 10; i++)
   {
      fprintf(ptr, "%d x %d = %d\n", num, i, num*i);
   }
   
   fclose(ptr);
   return 0;
}
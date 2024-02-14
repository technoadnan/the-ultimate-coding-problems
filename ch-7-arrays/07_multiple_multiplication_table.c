#include <stdio.h>

void multiplication_table(int multarr[], int num)
{
   for (int i = 1; i <= 10; i++)
   {
      multarr[i] = i * num;
   }

   for (int i = 1; i <= 10; i++)
   {
      printf("%d x %d = %d\n", num, i, multarr[i]);
   }
   
   
}

int main(int argc, char const *argv[]) {
   int arr[3][10];
   multiplication_table(arr[0], 2);
   printf("\n");
   multiplication_table(arr[1], 7);
   printf("\n");
   multiplication_table(arr[2], 9);
   printf("\n");

   
   return 0;
}
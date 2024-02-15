#include <stdio.h>

void multiplication_table(int multarr[], int num)
{
   for (int i = 1; i <= 10; i++)
   {
      multarr[i-1] = i * num;
   }

   for (int i = 1; i <= 10; i++)
   {
      printf("%d x %d = %d\n", num, i, multarr[i-1]);
   }
}

int main(int argc, char const *argv[])
{
   int arr[3][10];

   for (int i = 0; i < 3; i++)
   {
      printf("Write the %d number: ", i + 1);
      for (int j = 0; j < 10; j++)
      {
         scanf("%d", &arr[i][j]);
      }
   }

   for (int i = 0; i < 3; i++)
   {
      multiplication_table(arr[i], arr[i][0]);
      printf("\n");
   }

   return 0;
}

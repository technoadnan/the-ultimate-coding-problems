#include <stdio.h>

int main(int argc, char const *argv[]) {
   int arr[11]; // n - 1
   int num;
   printf("Enter the number: ");
   scanf("%d", &num);

   
   for (int i = 1; i <= 10; i++)
   {
      arr[i] = i * num;
   }
   
   for (int i = 1; i <= 10; i++)
   {
      printf("%d is %d\n", i, arr[i]);
   }
   
   return 0;
}
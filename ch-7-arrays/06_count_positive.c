#include <stdio.h>

int main(int argc, char const *argv[]) {
   int arr[5]= {-3,4,3,-342,4};
   int new_arr[5];
   int size = sizeof(arr) / 4;
   
   int j = 0;
   for (int i = 0; i < size; i++)
   {
      if (arr[i] > 0)
      {
         new_arr[j] = arr[i];
         j++;
      }
   }
   
   
   for (int i = 0; i < j; i++)
   {
      printf("%d\n", new_arr[i]);
   }
   
   
   return 0;
}
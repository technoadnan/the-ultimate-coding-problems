#include <stdio.h>

int reverse(int arr[], int size)
{
   int new_arr[size];
   // size - 1 e.g the last index of arr
   for (int i = size - 1, j = 0; i >= 0; i--, j++)
   {
      new_arr[j] = arr[i];
   }
   // returing local variable is not allowed in c
   // overwrite old array with new array
   for (int i = 0; i < size; i++)
   {
      arr[i] = new_arr[i];
   }
      
}


int main(int argc, char const *argv[]) {
   int arr[] ={34,34,5,465,45,32423,42};
   int size_arr = sizeof(arr) / 4; // calc size of array

   reverse(arr, size_arr); 
   for (int i = 0; i < size_arr; i++)
   {
      printf("%d\n", arr[i]);
   }
   
   return 0;
}
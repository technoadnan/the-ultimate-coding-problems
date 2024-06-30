#include <stdio.h>

int main(int argc, char const *argv[]) {
   int arr[2][3][4];

   for (int i = 0; i < 2; i++)
   {
      for (int j = 0; j < 3; j++)
      {
         for (int k = 0; k < 4; k++)
         {
            printf("The adress of arr[%d][%d][%d] is %u\n", i,j,k, &arr[i][j][k]);
         }
         
      }
      
   }
   

   // for (int i = 0; i < 2; i++)
   // {
   //    printf("The adress is %d %u\n", i, arr[i]);
   //    for (int j = 0; j < 3; j++)
   //    {
   //       printf("The adress is %d %u\n", j, arr[j]);
   //       for (int k = 0; k < 4; k++)
   //       {
   //          printf("The adress is %d %u\n", k, arr[k]);  
   //       }
   //    }
   // }
   
   return 0;
}
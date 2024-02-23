#include <stdio.h>

int main(int argc, char const *argv[]) {
   FILE *fptr;
   fptr = fopen("05_sal_double.txt","r");

   int num1, num2;
   int nums[10];

   
   int i;
   for ( i = 0; i < 3; i++)
   {
      fscanf(fptr,"%d",&nums[i]);
   }

   fptr = fopen("05_sal_double_upt.txt","w");
   for (int j = 0; j < 3; j++)
   {
      fprintf(fptr,"%d ",nums[j]*2);
   }


   return 0;
}
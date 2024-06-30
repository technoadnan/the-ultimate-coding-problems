#include <stdio.h>

int main(int argc, char const *argv[]) {
   int num, sum=0;
   printf("Enter the number: ");
   scanf("%d",&num);

   for (int i = 0; i <= 10; i++)
   {
      sum = sum + (num * i);
   }
   printf("the sum is %d", sum);

   
   return 0;
}
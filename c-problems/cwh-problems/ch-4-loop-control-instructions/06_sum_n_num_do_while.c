#include <stdio.h>

int main(int argc, char const *argv[]) {
   int sum=0,i=1,n;
   printf("Enter the digit: ");
   scanf("%d", &n);
   do
   {
      sum = sum + i;
      i++;
   } while (i <= n);
   
   printf("sum of n numbers: %d", sum);
   
   return 0;
}
#include <stdio.h>

int main(int argc, char const *argv[]) {
   int sum=0,i=1,n;
   printf("Enter the digit: ");
   scanf("%d", &n);
   while (i <= n)
   {
      sum = sum + i;
      i++;
   }
   printf("sum of n numbers: %d", sum);
   
   return 0;
}
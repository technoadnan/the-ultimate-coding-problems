#include <stdio.h>
int main(int argc, char const *argv[])
{
   float principal, rate;
   int time;

   printf("Principal: ");
   scanf("%f", &principal);

   printf("Rate: ");
   scanf("%f", &rate);

   printf("Time: ");
   scanf("%d", &time);

   float result = principal * (1 + rate/100 * time);
   printf("Final Amount: %.2f", result);

   return 0;
}

#include <stdio.h>
#include <math.h>

const double PI = 3.14159265359;
int main(int argc, char const *argv[])
{
   int radius;
   printf("Enter the radius ");
   scanf("%d",&radius);
   printf("%f", PI * pow(radius,2)); // make sure to print this with double(more precendence)
   return 0;
}
